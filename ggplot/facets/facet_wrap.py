from __future__ import annotations

from dataclasses import dataclass
from math import ceil

import pandas as pd

from ..exceptions import GGPlotError
from .facet import facet


@dataclass
class facet_wrap(facet):
    facets: str
    ncol: int | None = None

    def get_panels(self, df: pd.DataFrame):
        if self.facets not in df.columns:
            raise GGPlotError(f"facet_wrap: missing column {self.facets!r}")
        panels = []
        for key, sub in df.groupby(self.facets, dropna=False, sort=False):
            panels.append((str(key), sub))
        return panels

    def layout(self, n_panels: int) -> tuple[int, int]:
        if n_panels <= 0:
            return (1, 1)
        if self.ncol is None:
            ncol = int(ceil(n_panels**0.5))
        else:
            ncol = int(self.ncol)
        nrow = int(ceil(n_panels / ncol))
        return (nrow, ncol)
