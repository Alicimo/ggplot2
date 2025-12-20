from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_smooth import stat_smooth
from .geom import geom


@dataclass
class GeomSmooth(geom):
    def __post_init__(self):
        if self.stat is None:
            self.stat = stat_smooth()

    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []
        return [go.Scatter(x=df["x"], y=df["y"], mode="lines", showlegend=False)]


def geom_smooth(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomSmooth:
    mapping = mapping if mapping is not None else aes()
    g = GeomSmooth(mapping=mapping, data=data)
    g.stat = stat_smooth()
    g.params.update(kwargs)
    return g
