from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomRug(geom):
    def to_traces(self, df, *, plot):
        # Draw rug marks along x or y.
        # v0 supports x only.
        if "x" not in df.columns:
            return []
        # Use very short segments in paper coordinates via shapes.
        shapes = []
        for v in df["x"]:
            shapes.append(
                {
                    "type": "line",
                    "x0": v,
                    "x1": v,
                    "y0": 0,
                    "y1": 0.02,
                    "xref": "x",
                    "yref": "paper",
                    "line": {"color": "black"},
                }
            )
        if not hasattr(plot, "_shapes"):
            plot._shapes = []
        plot._shapes.extend(shapes)
        return []


def geom_rug(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomRug:
    mapping = mapping if mapping is not None else aes()
    g = GeomRug(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
