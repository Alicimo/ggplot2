from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomStep(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []

        direction = self.params.get("direction", "hv")
        # Plotly uses line.shape for step-like interpolation.
        # Supported: 'hv', 'vh', 'hvh', 'vhv'.
        if direction not in {"hv", "vh", "hvh", "vhv"}:
            direction = "hv"

        group_col = None
        if "group" in df.columns:
            group_col = "group"
        elif "color" in df.columns:
            group_col = "color"

        def _trace(sub, *, name: str | None):
            sub = sub.sort_values("x", kind="stable")
            line = {"shape": direction}
            if "color" in sub.columns:
                line["color"] = sub["color"].iloc[0]
            return go.Scatter(
                x=sub["x"],
                y=sub["y"],
                mode="lines",
                line=line,
                name=name,
            )

        if group_col is None:
            return [_trace(df, name=None)]

        traces = []
        for key, sub in df.groupby(group_col, dropna=False, sort=False):
            traces.append(_trace(sub, name=str(key)))
        return traces


def geom_step(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomStep:
    mapping = mapping if mapping is not None else aes()
    g = GeomStep(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
