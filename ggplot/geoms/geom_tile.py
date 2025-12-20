from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomTile(geom):
    def to_traces(self, df, *, plot):
        # Expect x, y, and optionally fill. Use a Heatmap as a first approximation.
        if "x" not in df.columns or "y" not in df.columns:
            return []
        if "fill" not in df.columns:
            # Treat as presence/1
            df = df.copy()
            df["fill"] = 1

        # pivot to matrix
        try:
            mat = df.pivot_table(index="y", columns="x", values="fill", aggfunc="first")
        except Exception:
            return []
        return [go.Heatmap(x=mat.columns.tolist(), y=mat.index.tolist(), z=mat.values)]


def geom_tile(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomTile:
    mapping = mapping if mapping is not None else aes()
    g = GeomTile(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
