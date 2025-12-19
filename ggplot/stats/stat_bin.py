from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class stat_bin(stat):
    def __init__(self, bins: int = 30):
        self.bins = bins

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns:
            raise GGPlotError("stat_bin requires x")
        x = pd.to_numeric(df["x"], errors="coerce")
        x = x.dropna()
        if x.empty:
            return pd.DataFrame({"x": [], "count": [], "xmin": [], "xmax": []})

        edges = np.histogram_bin_edges(x.to_numpy(), bins=self.bins)
        counts, _ = np.histogram(x.to_numpy(), bins=edges)
        mids = (edges[:-1] + edges[1:]) / 2
        out = pd.DataFrame(
            {
                "x": mids,
                "count": counts,
                "xmin": edges[:-1],
                "xmax": edges[1:],
            }
        )
        return out

