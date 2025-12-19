from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..positions.position_identity import position_identity
from ..positions.position_stack import position_stack
from ..positions.position_dodge import position_dodge
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

        # If stacking was computed, render using base + height.
        if "ymin" in df.columns and "ymax" in df.columns:
            base = df["ymin"]
            height = df["ymax"] - df["ymin"]
            return [go.Bar(x=df["x"], y=height, base=base)]

        return [go.Bar(x=df["x"], y=df[ycol])]


def geom_bar(
    mapping: Optional[aes] = None,
    data: Optional[Any] = None,
    *,
    stat: str = "count",
    position: str = "stack",
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

    if position == "stack":
        g.position = position_stack()
    elif position == "identity":
        g.position = position_identity()
    elif position == "dodge":
        g.position = position_dodge()
    else:
        raise ValueError(f"Unsupported position for geom_bar: {position!r}")

    g.params.update(kwargs)
    return g
