from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatSmooth(stat):
    """Minimal smoothing stat.

    v0 implementation: simple linear regression fit producing yhat over sorted x.
    """

    def __init__(self, n: int = 80, method: str = "linear"):
        self.n = n
        self.method = method

    def _lowess(self, x: np.ndarray, y: np.ndarray, frac: float = 0.4) -> np.ndarray:
        # Very small LOWESS-like smoother.
        n = x.size
        k = max(2, int(np.ceil(frac * n)))
        yhat = np.zeros_like(y)
        for i in range(n):
            # use k nearest neighbors in x
            dist = np.abs(x - x[i])
            idx = np.argpartition(dist, k - 1)[:k]
            xw = x[idx]
            yw = y[idx]
            # tricube weights
            dmax = float(dist[idx].max())
            if dmax == 0.0:
                yhat[i] = float(np.mean(yw))
                continue
            u = dist[idx] / dmax
            w = (1 - u**3) ** 3
            X = np.column_stack([np.ones_like(xw), xw])
            W = np.sqrt(w)
            beta, *_ = np.linalg.lstsq(X * W[:, None], yw * W, rcond=None)
            yhat[i] = float(beta[0] + beta[1] * x[i])
        return yhat

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_smooth requires x and y")
        x = pd.to_numeric(df["x"], errors="coerce")
        y = pd.to_numeric(df["y"], errors="coerce")
        mask = x.notna() & y.notna()
        x = x[mask].to_numpy(dtype=float)
        y = y[mask].to_numpy(dtype=float)
        if x.size < 2:
            return pd.DataFrame({"x": [], "y": []})

        order = np.argsort(x)
        x = x[order]
        y = y[order]

        xs = np.linspace(float(x.min()), float(x.max()), int(self.n))
        if self.method == "linear":
            A = np.vstack([x, np.ones_like(x)]).T
            coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
            slope, intercept = float(coef[0]), float(coef[1])
            ys = slope * xs + intercept
        elif self.method in {"lowess", "loess"}:
            # smooth on observed x then interpolate to grid
            yhat = self._lowess(x, y)
            ys = np.interp(xs, x, yhat)
        else:
            raise GGPlotError(f"Unsupported smoothing method: {self.method!r}")
        out = pd.DataFrame({"x": xs, "y": ys})
        return out


def stat_smooth(*, method: str = "linear") -> StatSmooth:
    return StatSmooth(method=method)
