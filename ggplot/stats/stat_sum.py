from __future__ import annotations

import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatSum(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_sum requires x and y")
        out = (
            df.groupby(["x", "y"], dropna=False, sort=False)
            .size()
            .reset_index(name="n")
        )
        return out


def stat_sum() -> StatSum:
    return StatSum()
