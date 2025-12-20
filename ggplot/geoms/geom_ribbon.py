from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from .._utils.scales import continuous_scale_info, try_as_numeric
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
                x=x,
                y=y,
                mode="lines",
                fill="toself",
                fillcolor=fillcolor,
                line={"color": linecolor},
                opacity=float(df["alpha"].iloc[0]) if "alpha" in df.columns else None,
                showlegend=False,
            )
        ]


def geom_ribbon(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomRibbon:
    mapping = mapping if mapping is not None else aes()
    g = GeomRibbon(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
