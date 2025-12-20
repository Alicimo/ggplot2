from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd
import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_density import stat_density
from .geom import geom


@dataclass
class GeomViolin(geom):
    def __post_init__(self):
        if self.stat is None:
            self.stat = stat_density()

    def to_traces(self, df, *, plot):
        # Expect x (optional), y (grid), density
        if "y" not in df.columns or "density" not in df.columns:
            return []
        if "x" not in df.columns:
            # single violin centered at 0
            x0 = 0.0
            x = list(x0 + df["density"]) + list(reversed(x0 - df["density"]))
            y = list(df["y"]) + list(reversed(df["y"]))
            return [go.Scatter(x=x, y=y, mode="lines", fill="toself", showlegend=False)]

        traces = []
        x_codes, x_uniques = pd.factorize(df["x"], sort=False)
        x_map = {val: float(i) for i, val in enumerate(x_uniques)}

        for xval, sub in df.groupby("x", dropna=False, sort=False):
            x0 = x_map.get(xval, 0.0)
            x = list(x0 + sub["density"].to_numpy()) + list(
                reversed(x0 - sub["density"].to_numpy())
            )
            y = list(sub["y"]) + list(reversed(sub["y"]))
            traces.append(
                go.Scatter(x=x, y=y, mode="lines", fill="toself", name=str(xval))
            )
        return traces


def geom_violin(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomViolin:
    mapping = mapping if mapping is not None else aes()
    g = GeomViolin(mapping=mapping, data=data)
    g.stat = stat_density()
    g.params.update(kwargs)
    return g
