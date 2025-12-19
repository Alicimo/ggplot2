from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import plotly.graph_objects as go

from ..mapping.aes import aes
from ..stats.stat_boxplot import stat_boxplot
from .geom import geom


@dataclass
class GeomBoxplot(geom):
    def __post_init__(self):
        if self.stat is None:
            self.stat = stat_boxplot()

    def to_traces(self, df, *, plot):
        required = {"lower", "middle", "upper", "ymin", "ymax"}
        if not required.issubset(df.columns):
            return []

        # Render as a box with whiskers using Scatter shapes.
        traces = []
        if "x" in df.columns:
            for _, row in df.iterrows():
                x = row["x"]
                # box
                traces.append(
                    go.Scatter(
                        x=[x, x, x, x, x],
                        y=[row["lower"], row["upper"], row["upper"], row["lower"], row["lower"]],
                        mode="lines",
                        showlegend=False,
                    )
                )
                # median
                traces.append(
                    go.Scatter(
                        x=[x, x],
                        y=[row["middle"], row["middle"]],
                        mode="lines",
                        showlegend=False,
                    )
                )
                # whiskers
                traces.append(go.Scatter(x=[x, x], y=[row["ymin"], row["lower"]], mode="lines", showlegend=False))
                traces.append(go.Scatter(x=[x, x], y=[row["upper"], row["ymax"]], mode="lines", showlegend=False))
        else:
            row = df.iloc[0]
            traces.append(
                go.Box(
                    q1=[row["lower"]],
                    median=[row["middle"]],
                    q3=[row["upper"]],
                    lowerfence=[row["ymin"]],
                    upperfence=[row["ymax"]],
                    showlegend=False,
                )
            )
        return traces


def geom_boxplot(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomBoxplot:
    mapping = mapping if mapping is not None else aes()
    g = GeomBoxplot(mapping=mapping, data=data)
    g.stat = stat_boxplot()
    g.params.update(kwargs)
    return g

