from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomCrossbar(geom):
    def to_traces(self, df, *, plot):
        needed = {"x", "ymin", "ymax", "y"}
        if not needed.issubset(df.columns):
            return []

        width = float(self.params.get("width", 0.5))
        traces = []
        for _, row in df.iterrows():
            x0 = float(row["x"])
            xmin = x0 - width / 2
            xmax = x0 + width / 2
            ymin = float(row["ymin"])
            ymax = float(row["ymax"])
            y = float(row["y"])

            fillcolor = None
            if "fill" in df.columns:
                fillcolor = row.get("fill")

            # filled rectangle
            traces.append(
                go.Scatter(
                    x=[xmin, xmin, xmax, xmax, xmin],
                    y=[ymin, ymax, ymax, ymin, ymin],
                    mode="lines",
                    fill="toself",
                    fillcolor=fillcolor,
                    showlegend=False,
                )
            )
            # middle bar
            traces.append(
                go.Scatter(
                    x=[xmin, xmax],
                    y=[y, y],
                    mode="lines",
                    showlegend=False,
                )
            )

        return traces


def geom_crossbar(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomCrossbar:
    mapping = mapping if mapping is not None else aes()
    g = GeomCrossbar(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
