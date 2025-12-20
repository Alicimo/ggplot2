from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomSpoke(geom):
    def to_traces(self, df, *, plot):
        needed = {"x", "y", "angle", "radius"}
        if not needed.issubset(df.columns):
            return []

        x = []
        y = []
        for _, row in df.iterrows():
            x0 = float(row["x"])
            y0 = float(row["y"])
            angle = float(row["angle"])
            radius = float(row["radius"])
            x1 = x0 + radius * float(np.cos(angle))
            y1 = y0 + radius * float(np.sin(angle))
            x.extend([x0, x1, None])
            y.extend([y0, y1, None])

        line = {}
        if "color" in df.columns:
            line["color"] = df["color"].iloc[0]

        return [go.Scatter(x=x, y=y, mode="lines", line=line, showlegend=False)]


def geom_spoke(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomSpoke:
    mapping = mapping if mapping is not None else aes()
    g = GeomSpoke(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
