from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomVLine(geom):
    def to_traces(self, df, *, plot):
        if "xintercept" not in df.columns:
            return []

        shapes = []
        for v in df["xintercept"]:
            shapes.append(
                {
                    "type": "line",
                    "x0": v,
                    "x1": v,
                    "y0": 0,
                    "y1": 1,
                    "xref": "x",
                    "yref": "paper",
                    "line": {"color": "black"},
                }
            )

        if not hasattr(plot, "_shapes"):
            plot._shapes = []
        plot._shapes.extend(shapes)

        return []


def geom_vline(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomVLine:
    mapping = mapping if mapping is not None else aes()
    g = GeomVLine(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
