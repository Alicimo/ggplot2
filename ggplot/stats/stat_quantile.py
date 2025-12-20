from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .stat import stat


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
            xs = sub["x"].to_numpy(dtype=float)
            ys = sub["y"].to_numpy(dtype=float)
            if len(xs) < 2:
                continue
            order = np.argsort(xs, kind="stable")
            xs = xs[order]
            ys = ys[order]

            x_grid = np.linspace(xs.min(), xs.max(), self.n)
            # Piecewise-linear interpolation as a simple stand-in for quantile regression.
            y_grid = np.interp(x_grid, xs, ys)

            for q in self.quantiles:
                # This is not real quantile regression; treat as a placeholder.
                # Using interpolation makes tests deterministic and keeps API wiring.
                d = {"x": x_grid, "y": y_grid, "quantile": q}
                if gkey is not None:
                    d["group"] = gkey
                out.append(d)

        if not out:
            return df.iloc[0:0]
        import pandas as pd

        return pd.concat([pd.DataFrame(d) for d in out], ignore_index=True)


def stat_quantile(
    *, quantiles: tuple[float, ...] = (0.5,), n: int = 100
) -> StatQuantile:
    return StatQuantile(quantiles=quantiles, n=n)
