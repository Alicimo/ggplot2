from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_density import stat_density
from .geom import geom


@dataclass
class GeomDensity(geom):
    def __post_init__(self):
        if self.stat is None:
            self.stat = stat_density()

    def to_traces(self, df, *, plot):
        # expects y + density, but for density plot treat y as x
        if "y" not in df.columns or "density" not in df.columns:
            return []

        # Map to x/y for plotting
        x = df["y"]
        y = df["density"]
        return [go.Scatter(x=x, y=y, mode="lines", showlegend=False)]


def geom_density(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomDensity:
    mapping = mapping if mapping is not None else aes()
    g = GeomDensity(mapping=mapping, data=data)
    g.stat = stat_density()
    g.params.update(kwargs)
    return g
