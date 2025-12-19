from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .facet import facet


@dataclass
class facet_null(facet):
    def get_panels(self, df: pd.DataFrame):
        return [("", df)]

