from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatPointdensity(stat):
    def __init__(self, k: int = 5):
        self.k = int(k)

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_pointdensity requires x and y")
        x = pd.to_numeric(df["x"], errors="coerce").to_numpy(dtype=float)
        y = pd.to_numeric(df["y"], errors="coerce").to_numpy(dtype=float)
        mask = np.isfinite(x) & np.isfinite(y)
        x = x[mask]
        y = y[mask]
        if x.size == 0:
            return pd.DataFrame({"x": [], "y": [], "density": []})
        if x.size < 2:
            return pd.DataFrame({"x": x, "y": y, "density": np.ones_like(x)})

        pts = np.column_stack([x, y])
        d2 = ((pts[:, None, :] - pts[None, :, :]) ** 2).sum(axis=2)
        np.fill_diagonal(d2, np.inf)
        k = max(1, min(self.k, x.size - 1))
        kth = np.partition(d2, k - 1, axis=1)[:, k - 1]
        dens = 1.0 / np.sqrt(kth)
        dens[np.isinf(dens)] = 0.0
        return pd.DataFrame({"x": x, "y": y, "density": dens})


def stat_pointdensity(*, k: int = 5) -> StatPointdensity:
    return StatPointdensity(k=k)
