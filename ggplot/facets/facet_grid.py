from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Optional

import pandas as pd

from ..exceptions import GGPlotError
from .facet import facet


@dataclass
class facet_grid(facet):
    rows: Optional[str] = None
    cols: Optional[str] = None

    def get_panels(self, df: pd.DataFrame):
        if self.rows is None and self.cols is None:
            return [("", df)]

        if self.rows is not None and self.rows not in df.columns:
            raise GGPlotError(f"facet_grid: missing column {self.rows!r}")
        if self.cols is not None and self.cols not in df.columns:
            raise GGPlotError(f"facet_grid: missing column {self.cols!r}")

        # Build grid of unique values
        row_vals = [""] if self.rows is None else list(pd.unique(df[self.rows]))
        col_vals = [""] if self.cols is None else list(pd.unique(df[self.cols]))

        panels = []
        for rv in row_vals:
            for cv in col_vals:
                sub = df
                title_parts = []
                if self.rows is not None:
                    sub = sub[sub[self.rows] == rv]
                    title_parts.append(f"{self.rows}={rv}")
                if self.cols is not None:
                    sub = sub[sub[self.cols] == cv]
                    title_parts.append(f"{self.cols}={cv}")
                panels.append((", ".join(title_parts), sub))
        return panels

    def layout(self, n_panels: int) -> tuple[int, int]:
        if self.rows is None and self.cols is None:
            return (1, 1)
        # Determine rows/cols from unique values when possible.
        # Caller provides n_panels, so choose a square-ish layout as fallback.
        ncol = int(ceil(n_panels ** 0.5))
        nrow = int(ceil(n_panels / ncol))
        return (nrow, ncol)

