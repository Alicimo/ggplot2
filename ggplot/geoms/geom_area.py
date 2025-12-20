from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from .._utils.scales import continuous_scale_info, try_as_numeric
from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomArea(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []
        df = df.sort_values("x", kind="stable")
        fillcolor = "rgba(0,0,0,0.2)"
        if "fill" in df.columns and not df.empty:
            info = continuous_scale_info(plot, "fill")
            f = try_as_numeric(df["fill"])
            fillcolor = df["fill"].iloc[0] if info is None or f is None else float(f[0])
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
                opacity=float(df["alpha"].iloc[0]) if "alpha" in df.columns else None,
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
