from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_bin import stat_bin
from .geom import geom


@dataclass
class GeomFreqpoly(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns:
            return []
        ycol = "count" if "count" in df.columns else "y" if "y" in df.columns else None
        if ycol is None:
            return []

        group_col = None
        if "group" in df.columns:
            group_col = "group"
        elif "color" in df.columns:
            group_col = "color"

        def _trace(sub, *, name: str | None):
            sub = sub.sort_values("x", kind="stable")
            line = {}
            if "color" in sub.columns:
                line["color"] = sub["color"].iloc[0]
            return go.Scatter(
                x=sub["x"],
                y=sub[ycol],
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


def geom_freqpoly(
    mapping: aes | None = None,
    data: Any | None = None,
    *,
    bins: int = 30,
    **kwargs: Any,
) -> GeomFreqpoly:
    mapping = mapping if mapping is not None else aes()
    g = GeomFreqpoly(mapping=mapping, data=data)
    g.stat = stat_bin(bins=bins)
    g.params.update(kwargs)
    return g
