from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomLine(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []
        line = {}
        if "color" in df.columns:
            line["color"] = df["color"]
        return [go.Scatter(x=df["x"], y=df["y"], mode="lines", line=line)]


def geom_line(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomLine:
    mapping = mapping if mapping is not None else aes()
    g = GeomLine(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

