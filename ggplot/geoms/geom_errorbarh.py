from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomErrorbarh(geom):
    def to_traces(self, df, *, plot):
        needed = {"y", "xmin", "xmax"}
        if not needed.issubset(df.columns):
            return []

        height = float(self.params.get("height", 0.1))
        x = []
        y = []
        for _, row in df.iterrows():
            y0 = float(row["y"])
            xmin = float(row["xmin"])
            xmax = float(row["xmax"])
            # horizontal line
            x.extend([xmin, xmax, None])
            y.extend([y0, y0, None])
            # caps
            x.extend([xmin, xmin, None])
            y.extend([y0 - height, y0 + height, None])
            x.extend([xmax, xmax, None])
            y.extend([y0 - height, y0 + height, None])

        return [go.Scatter(x=x, y=y, mode="lines", showlegend=False)]


def geom_errorbarh(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomErrorbarh:
    mapping = mapping if mapping is not None else aes()
    g = GeomErrorbarh(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
