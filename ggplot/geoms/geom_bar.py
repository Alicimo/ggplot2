from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_count import stat_count
from .geom import geom


@dataclass
class GeomBar(geom):
    def __post_init__(self):
        # Default stat for bars is count, matching ggplot2/plotnine behavior.
        if self.stat is None:
            self.stat = stat_count()

    def to_traces(self, df, *, plot):
        if "x" not in df.columns:
            return []
        ycol = "y" if "y" in df.columns else "count" if "count" in df.columns else None
        if ycol is None:
            return []
        return [go.Bar(x=df["x"], y=df[ycol])]


def geom_bar(
    mapping: Optional[aes] = None,
    data: Optional[Any] = None,
    *,
    stat: str = "count",
    **kwargs: Any,
) -> GeomBar:
    mapping = mapping if mapping is not None else aes()
    g = GeomBar(mapping=mapping, data=data)

    if stat == "count":
        g.stat = stat_count()
    elif stat == "identity":
        # identity: expect y to be mapped/provided
        from ..stats.stat_identity import stat_identity

        g.stat = stat_identity()
    else:
        raise ValueError(f"Unsupported stat for geom_bar: {stat!r}")

    g.params.update(kwargs)
    return g

