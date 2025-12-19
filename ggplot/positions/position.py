from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class position:
    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        return df

