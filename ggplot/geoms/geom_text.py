from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomText(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns or "label" not in df.columns:
            return []
        textfont = {}
        if "color" in df.columns:
            textfont["color"] = df["color"]
        if "size" in df.columns:
            textfont["size"] = df["size"]
        opacity = float(df["alpha"].iloc[0]) if "alpha" in df.columns else None
        return [
            go.Scatter(
                x=df["x"],
                y=df["y"],
                mode="text",
                text=df["label"],
                textfont=textfont,
                opacity=opacity,
            )
        ]


def geom_text(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomText:
    mapping = mapping if mapping is not None else aes()
    g = GeomText(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
