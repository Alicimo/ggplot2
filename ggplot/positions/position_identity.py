from __future__ import annotations

import pandas as pd

from .position import position


class position_identity(position):
    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        return df
