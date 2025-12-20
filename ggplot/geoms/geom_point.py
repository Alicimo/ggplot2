from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomPoint(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []
        if "color" in df.columns:
            traces = []
            for key, sub in df.groupby("color", dropna=False, sort=False):
                marker = {"color": key}
                if "size" in sub.columns:
                    marker["size"] = sub["size"]
                # Prefer original discrete label if present.
                name = (
                    sub["colour"].iloc[0]
                    if "colour" in sub.columns and not sub.empty
                    else key
                )
                traces.append(
                    go.Scatter(
                        x=sub["x"],
                        y=sub["y"],
                        mode="markers",
                        marker=marker,
                        name=str(name),
                    )
                )
            return traces

        marker = {}
        if "size" in df.columns:
            marker["size"] = df["size"]
        return [go.Scatter(x=df["x"], y=df["y"], mode="markers", marker=marker)]


def geom_point(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomPoint:
    mapping = mapping if mapping is not None else aes()
    g = GeomPoint(mapping=mapping, data=data)
    if "position" in kwargs:
        g.position = kwargs.pop("position")
    g.params.update(kwargs)
    return g
