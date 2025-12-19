from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomSegment(geom):
    def to_traces(self, df, *, plot):
        # expects x,y,xend,yend
        needed = {"x", "y", "xend", "yend"}
        if not needed.issubset(df.columns):
            return []

        x = []
        y = []
        for _, row in df.iterrows():
            x.extend([row["x"], row["xend"], None])
            y.extend([row["y"], row["yend"], None])

        line = {}
        if "color" in df.columns:
            # single color only for v0
            line["color"] = df["color"].iloc[0]

        return [go.Scatter(x=x, y=y, mode="lines", line=line, showlegend=False)]


def geom_segment(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomSegment:
    mapping = mapping if mapping is not None else aes()
    g = GeomSegment(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

