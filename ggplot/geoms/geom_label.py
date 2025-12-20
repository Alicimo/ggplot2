from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomLabel(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns or "label" not in df.columns:
            return []

        textfont = {}
        if "color" in df.columns:
            textfont["color"] = df["color"]

        marker = {}
        if "fill" in df.columns:
            marker["color"] = df["fill"]
        if "alpha" in df.columns:
            marker["opacity"] = df["alpha"]

        return [
            go.Scatter(
                x=df["x"],
                y=df["y"],
                mode="markers+text",
                marker={"symbol": "square", **marker},
                text=df["label"],
                textposition="middle center",
                textfont=textfont,
                showlegend=False,
            )
        ]


def geom_label(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomLabel:
    mapping = mapping if mapping is not None else aes()
    g = GeomLabel(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
