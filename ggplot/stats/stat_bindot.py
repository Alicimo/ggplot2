from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatBindot(stat):
    def __init__(self, bins: int = 30):
        self.bins = int(bins)

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns:
            raise GGPlotError("stat_bindot requires x")
        x = pd.to_numeric(df["x"], errors="coerce").dropna().to_numpy(dtype=float)
        if x.size == 0:
            return pd.DataFrame({"x": [], "count": []})

        edges = np.histogram_bin_edges(x, bins=self.bins)
        counts, _ = np.histogram(x, bins=edges)
        mids = (edges[:-1] + edges[1:]) / 2
        return pd.DataFrame(
            {"x": mids, "count": counts, "xmin": edges[:-1], "xmax": edges[1:]}
        )


def stat_bindot(*, bins: int = 30) -> StatBindot:
    return StatBindot(bins=bins)
