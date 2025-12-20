from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_count import stat_count
from .geom import geom


@dataclass
class GeomCount(geom):
    def __post_init__(self):
        if self.stat is None:
            self.stat = stat_count()

    def to_traces(self, df, *, plot):
        # Minimal: render as scatter points at (x, y) with size mapped from `count`.
        # plotnine computes `count` from x (and optionally other aesthetics).
        if "x" not in df.columns:
            return []

        ycol = "y" if "y" in df.columns else "count" if "count" in df.columns else None
        if ycol is None:
            return []

        size_col = "count" if "count" in df.columns else None
        marker = {}
        if size_col is not None:
            marker["size"] = df[size_col]
            marker["sizemode"] = "area"

        if "color" in df.columns:
            marker["color"] = df["color"]

        return [go.Scatter(x=df["x"], y=df[ycol], mode="markers", marker=marker)]


def geom_count(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomCount:
    mapping = mapping if mapping is not None else aes()
    g = GeomCount(mapping=mapping, data=data)
    g.stat = stat_count()
    g.params.update(kwargs)
    return g
