from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomLineRange(geom):
    def to_traces(self, df, *, plot):
        needed = {"x", "ymin", "ymax"}
        if not needed.issubset(df.columns):
            return []
        x = []
        y = []
        for _, row in df.iterrows():
            x.extend([row["x"], row["x"], None])
            y.extend([row["ymin"], row["ymax"], None])
        return [go.Scatter(x=x, y=y, mode="lines", showlegend=False)]


def geom_linerange(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomLineRange:
    mapping = mapping if mapping is not None else aes()
    g = GeomLineRange(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

