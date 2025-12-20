from __future__ import annotations

from dataclasses import dataclass

import pandas as pd


@dataclass
class facet:
    def get_panels(self, df: pd.DataFrame) -> list[tuple[str, pd.DataFrame]]:
        return [("", df)]

    def __radd__(self, other):
        other.facet = self
        return other
