from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomDensity2d(geom):
    def to_traces(self, df, *, plot):
        # Minimal: expects stat_density_2d-style output with x/y and group.
        if "x" not in df.columns or "y" not in df.columns:
            return []

        group_col = "group" if "group" in df.columns else None
        if group_col is None:
            return [go.Scatter(x=df["x"], y=df["y"], mode="lines")]

        traces = []
        for key, sub in df.groupby(group_col, dropna=False, sort=False):
            traces.append(
                go.Scatter(x=sub["x"], y=sub["y"], mode="lines", name=str(key))
            )
        return traces


def geom_density_2d(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomDensity2d:
    mapping = mapping if mapping is not None else aes()
    g = GeomDensity2d(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
