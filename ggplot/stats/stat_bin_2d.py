from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatBin2D(stat):
    def __init__(self, bins: int = 30):
        self.bins = int(bins)

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_bin_2d requires x and y")

        x = pd.to_numeric(df["x"], errors="coerce").to_numpy(dtype=float)
        y = pd.to_numeric(df["y"], errors="coerce").to_numpy(dtype=float)
        mask = np.isfinite(x) & np.isfinite(y)
        x = x[mask]
        y = y[mask]
        if x.size == 0:
            return pd.DataFrame({"x": [], "y": [], "count": []})

        counts, xedges, yedges = np.histogram2d(x, y, bins=self.bins)
        xcenters = (xedges[:-1] + xedges[1:]) / 2
        ycenters = (yedges[:-1] + yedges[1:]) / 2

        xs, ys = np.meshgrid(xcenters, ycenters, indexing="xy")
        out = pd.DataFrame(
            {
                "x": xs.ravel(),
                "y": ys.ravel(),
                "count": counts.T.ravel(),
            }
        )
        out["fill"] = out["count"]
        return out


def stat_bin_2d(*, bins: int = 30) -> StatBin2D:
    return StatBin2D(bins=bins)


def stat_bin2d(*, bins: int = 30) -> StatBin2D:
    return StatBin2D(bins=bins)
