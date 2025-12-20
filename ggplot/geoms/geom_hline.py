from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomHLine(geom):
    def to_traces(self, df, *, plot):
        if "yintercept" not in df.columns:
            return []

        shapes = []
        for v in df["yintercept"]:
            shapes.append(
                {
                    "type": "line",
                    "x0": 0,
                    "x1": 1,
                    "y0": v,
                    "y1": v,
                    "xref": "paper",
                    "yref": "y",
                    "line": {"color": "black"},
                }
            )
        if not hasattr(plot, "_shapes"):
            plot._shapes = []
        plot._shapes.extend(shapes)
        return []


def geom_hline(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomHLine:
    mapping = mapping if mapping is not None else aes()
    g = GeomHLine(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
