from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomRibbon(geom):
    def to_traces(self, df, *, plot):
        needed = {"x", "ymin", "ymax"}
        if not needed.issubset(df.columns):
            return []

        df = df.sort_values("x", kind="stable")
        x = list(df["x"]) + list(reversed(df["x"]))
        y = list(df["ymax"]) + list(reversed(df["ymin"]))
        fillcolor = df["fill"].iloc[0] if "fill" in df.columns and not df.empty else "rgba(0,0,0,0.2)"
        linecolor = df["color"].iloc[0] if "color" in df.columns and not df.empty else "rgba(0,0,0,0)"
        return [
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                fill="toself",
                fillcolor=fillcolor,
                line={"color": linecolor},
                showlegend=False,
            )
        ]


def geom_ribbon(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomRibbon:
    mapping = mapping if mapping is not None else aes()
    g = GeomRibbon(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

