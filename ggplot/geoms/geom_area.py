from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomArea(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []
        df = df.sort_values("x", kind="stable")
        fillcolor = (
            df["fill"].iloc[0]
            if "fill" in df.columns and not df.empty
            else "rgba(0,0,0,0.2)"
        )
        linecolor = (
            df["color"].iloc[0]
            if "color" in df.columns and not df.empty
            else "rgba(0,0,0,0)"
        )
        return [
            go.Scatter(
                x=df["x"],
                y=df["y"],
                mode="lines",
                fill="tozeroy",
                fillcolor=fillcolor,
                line={"color": linecolor},
                showlegend=False,
            )
        ]


def geom_area(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomArea:
    mapping = mapping if mapping is not None else aes()
    g = GeomArea(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
