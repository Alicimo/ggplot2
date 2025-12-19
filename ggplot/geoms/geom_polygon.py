from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

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
            fillcolor = df["fill"].iloc[0]

        if group_col is None:
            return [go.Scatter(x=df["x"], y=df["y"], mode="lines", fill="toself", fillcolor=fillcolor)]

        traces = []
        for key, sub in df.groupby(group_col, dropna=False, sort=False):
            fc = sub["fill"].iloc[0] if "fill" in sub.columns and not sub.empty else fillcolor
            traces.append(go.Scatter(x=sub["x"], y=sub["y"], mode="lines", fill="toself", fillcolor=fc, name=str(key)))
        return traces


def geom_polygon(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomPolygon:
    mapping = mapping if mapping is not None else aes()
    g = GeomPolygon(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

