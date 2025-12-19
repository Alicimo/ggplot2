from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomRect(geom):
    def to_traces(self, df, *, plot):
        needed = {"xmin", "xmax", "ymin", "ymax"}
        if not needed.issubset(df.columns):
            return []

        traces = []
        for _, row in df.iterrows():
            fillcolor = row["fill"] if "fill" in df.columns else "rgba(0,0,0,0)"
            linecolor = row["color"] if "color" in df.columns else "rgba(0,0,0,1)"
            traces.append(
                go.Scatter(
                    x=[row["xmin"], row["xmax"], row["xmax"], row["xmin"], row["xmin"]],
                    y=[row["ymin"], row["ymin"], row["ymax"], row["ymax"], row["ymin"]],
                    mode="lines",
                    fill="toself",
                    fillcolor=fillcolor,
                    line={"color": linecolor},
                    showlegend=False,
                )
            )
        return traces


def geom_rect(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomRect:
    mapping = mapping if mapping is not None else aes()
    g = GeomRect(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

