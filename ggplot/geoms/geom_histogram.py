from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_bin import stat_bin
from .geom import geom


@dataclass
class GeomHistogram(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "count" not in df.columns:
            return []
        # Render pre-binned histogram as bars.
        return [go.Bar(x=df["x"], y=df["count"])]


def geom_histogram(
    mapping: aes | None = None,
    data: Any | None = None,
    *,
    bins: int = 30,
    **kwargs: Any,
) -> GeomHistogram:
    mapping = mapping if mapping is not None else aes()
    g = GeomHistogram(mapping=mapping, data=data)
    g.stat = stat_bin(bins=bins)
    g.params.update(kwargs)
    return g
