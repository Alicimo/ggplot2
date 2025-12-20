from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from .._utils.scales import continuous_scale_info, try_as_numeric
from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomPolygon(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []

        group_col = "group" if "group" in df.columns else None
        fillcolor = None
        if "fill" in df.columns and not df.empty:
            info = continuous_scale_info(plot, "fill")
            f = try_as_numeric(df["fill"])
            if info is not None and f is not None:
                # Use the first value to pick a representative color.
                # Plotly doesn't support per-vertex fill gradients.
                fillcolor = float(f[0])
            else:
                fillcolor = df["fill"].iloc[0]

        if group_col is None:
            return [
                go.Scatter(
                    x=df["x"],
                    y=df["y"],
                    mode="lines",
                    fill="toself",
                    fillcolor=fillcolor,
                    opacity=float(df["alpha"].iloc[0])
                    if "alpha" in df.columns
                    else None,
                )
            ]

        traces = []
        for key, sub in df.groupby(group_col, dropna=False, sort=False):
            fc = (
                sub["fill"].iloc[0]
                if "fill" in sub.columns and not sub.empty
                else fillcolor
            )
            traces.append(
                go.Scatter(
                    x=sub["x"],
                    y=sub["y"],
                    mode="lines",
                    fill="toself",
                    fillcolor=fc,
                    name=str(key),
                    opacity=float(sub["alpha"].iloc[0])
                    if "alpha" in sub.columns
                    else None,
                )
            )
        return traces


def geom_polygon(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomPolygon:
    mapping = mapping if mapping is not None else aes()
    g = GeomPolygon(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
