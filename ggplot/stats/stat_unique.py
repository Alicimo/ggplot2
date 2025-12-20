from __future__ import annotations

import pandas as pd

from .stat import stat


class StatUnique(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        # Keep the first occurrence of each (x, y) pair if present.
        cols = [c for c in ("x", "y") if c in df.columns]
        if not cols:
            return df
        return df.drop_duplicates(subset=cols, keep="first")


def stat_unique() -> StatUnique:
    return StatUnique()
