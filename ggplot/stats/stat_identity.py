from __future__ import annotations

import pandas as pd

from .stat import stat


class stat_identity(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        return df
