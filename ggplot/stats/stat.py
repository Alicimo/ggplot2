from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd


@dataclass
class stat:
    """Base stat.

    Subclasses implement `compute(df, mapping)` and return a DataFrame.
    """

    def compute(self, df: pd.DataFrame, *, mapping: dict[str, Any]) -> pd.DataFrame:
        return df

