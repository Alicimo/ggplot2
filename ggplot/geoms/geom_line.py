from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomLine(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []

        group_col = None
        if "group" in df.columns:
            group_col = "group"
        elif "color" in df.columns:
            group_col = "color"

        if group_col is None:
            return [go.Scatter(x=df["x"], y=df["y"], mode="lines")]

        traces = []
        for key, sub in df.groupby(group_col, dropna=False, sort=False):
            sub = sub.sort_values("x", kind="stable")
            line = {}
            if "color" in sub.columns:
                # if color scale already applied, key may be a color value
                line["color"] = sub["color"].iloc[0]
            traces.append(
                go.Scatter(
                    x=sub["x"],
                    y=sub["y"],
                    mode="lines",
                    line=line,
                    name=str(key),
                )
            )
        return traces


def geom_line(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomLine:
    mapping = mapping if mapping is not None else aes()
    g = GeomLine(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
