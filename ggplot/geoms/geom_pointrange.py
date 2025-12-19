from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomPointrange(geom):
    def to_traces(self, df, *, plot):
        # expects x, y, ymin, ymax
        needed = {"x", "y"}
        if not needed.issubset(df.columns):
            return []

        if "ymin" in df.columns and "ymax" in df.columns:
            err = dict(type="data", symmetric=False, array=df["ymax"] - df["y"], arrayminus=df["y"] - df["ymin"])
            return [go.Scatter(x=df["x"], y=df["y"], mode="markers", error_y=err, showlegend=False)]
        return [go.Scatter(x=df["x"], y=df["y"], mode="markers", showlegend=False)]


def geom_pointrange(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomPointrange:
    mapping = mapping if mapping is not None else aes()
    g = GeomPointrange(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

