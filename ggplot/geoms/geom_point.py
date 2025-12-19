from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomPoint(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []
        marker = {}
        if "color" in df.columns:
            marker["color"] = df["color"]
        if "size" in df.columns:
            marker["size"] = df["size"]

        return [go.Scatter(x=df["x"], y=df["y"], mode="markers", marker=marker)]


def geom_point(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomPoint:
    mapping = mapping if mapping is not None else aes()
    g = GeomPoint(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
