from __future__ import annotations

import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class stat_count(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns:
            raise GGPlotError("stat_count requires x")
        group_cols = ["x"]
        # If `fill` is present, count within each fill group too.
        if "fill" in df.columns:
            group_cols.append("fill")
        out = (
            df.groupby(group_cols, dropna=False, sort=False)
            .size()
            .reset_index(name="count")
        )
        return out
