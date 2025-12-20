from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomErrorbar(geom):
    def to_traces(self, df, *, plot):
        needed = {"x", "ymin", "ymax"}
        if not needed.issubset(df.columns):
            return []
        width = float(self.params.get("width", 0.1))
        x = []
        y = []
        for _, row in df.iterrows():
            x0 = float(row["x"])
            ymin = float(row["ymin"])
            ymax = float(row["ymax"])
            # vertical line
            x.extend([x0, x0, None])
            y.extend([ymin, ymax, None])
            # caps
            x.extend([x0 - width, x0 + width, None])
            y.extend([ymin, ymin, None])
            x.extend([x0 - width, x0 + width, None])
            y.extend([ymax, ymax, None])
        return [go.Scatter(x=x, y=y, mode="lines", showlegend=False)]


def geom_errorbar(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomErrorbar:
    mapping = mapping if mapping is not None else aes()
    g = GeomErrorbar(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
