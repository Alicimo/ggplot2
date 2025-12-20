from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd

from .stat import stat


def _weighted_quantile_residual(u: np.ndarray, tau: float) -> np.ndarray:
    # Check loss derivative-ish: tau for positive residuals, (tau-1) for negative.
    return np.where(u >= 0, tau, tau - 1.0)


def _quantile_regression_irls(
    x: np.ndarray,
    y: np.ndarray,
    tau: float,
    *,
    max_iter: int = 200,
    tol: float = 1e-8,
) -> tuple[float, float]:
    """Very small IRLS quantile regression for y ~ a + b*x.

    This is not as robust/feature-complete as statsmodels, but is deterministic
    and avoids additional dependencies.
    """

    x = x.astype(float)
    y = y.astype(float)
    X = np.column_stack([np.ones_like(x), x])

    # Initial OLS.
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)

    eps = 1e-9
    for _ in range(max_iter):
        r = y - X @ beta
        w = np.abs(_weighted_quantile_residual(r, tau)) / np.maximum(np.abs(r), eps)
        W = np.sqrt(w)
        Xw = X * W[:, None]
        yw = y * W
        beta_new, *_ = np.linalg.lstsq(Xw, yw, rcond=None)
        if float(np.max(np.abs(beta_new - beta))) < tol:
            beta = beta_new
            break
        beta = beta_new

    intercept = float(beta[0])
    slope = float(beta[1])
    return intercept, slope


@dataclass
class StatQuantile(stat):
    quantiles: tuple[float, ...] = (0.5,)
    n: int = 100

    def compute(self, df, mapping: dict[str, Any]):
        if "x" not in df.columns or "y" not in df.columns:
            return df
        out = []
        group_col = "group" if "group" in df.columns else None
        groups = (
            [(None, df)] if group_col is None else df.groupby(group_col, dropna=False)
        )
        for gkey, sub in groups:
            xs = pd.to_numeric(sub["x"], errors="coerce").to_numpy(dtype=float)
            ys = pd.to_numeric(sub["y"], errors="coerce").to_numpy(dtype=float)
            mask = np.isfinite(xs) & np.isfinite(ys)
            xs = xs[mask]
            ys = ys[mask]
            if xs.size < 2:
                continue

            x_grid = np.linspace(float(xs.min()), float(xs.max()), int(self.n))
            for q in self.quantiles:
                intercept, slope = _quantile_regression_irls(xs, ys, float(q))
                y_grid = slope * x_grid + intercept
                d = {"x": x_grid, "y": y_grid, "quantile": q}
                if gkey is not None:
                    d["group"] = gkey
                out.append(d)

        if not out:
            return df.iloc[0:0]
        return pd.concat([pd.DataFrame(d) for d in out], ignore_index=True)


def stat_quantile(
    *, quantiles: tuple[float, ...] = (0.5,), n: int = 100
) -> StatQuantile:
    return StatQuantile(quantiles=quantiles, n=n)
