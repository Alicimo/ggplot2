from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

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
        return [go.Scatter(x=df["x"], y=df["y"], mode="text", text=df["label"], textfont=textfont)]


def geom_text(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomText:
    mapping = mapping if mapping is not None else aes()
    g = GeomText(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

