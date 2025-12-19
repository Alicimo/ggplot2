from __future__ import annotations

import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class stat_count(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns:
            raise GGPlotError("stat_count requires x")
        out = df.groupby("x", dropna=False, sort=False).size().reset_index(name="count")
        return out

