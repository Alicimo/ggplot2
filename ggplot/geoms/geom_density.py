from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from .._utils.scales import continuous_scale_info, try_as_numeric
from ..mapping.aes import aes
from ..stats.stat_density import stat_density
from .geom import geom


@dataclass
class GeomDensity(geom):
    def __post_init__(self):
        if self.stat is None:
            self.stat = stat_density()

    def to_traces(self, df, *, plot):
        # expects y + density, but for density plot treat y as x
        if "y" not in df.columns or "density" not in df.columns:
            return []

        # Map to x/y for plotting
        x = df["y"]
        y = df["density"]
        line = {}
        if "color" in df.columns:
            info = continuous_scale_info(plot, "color")
            c = try_as_numeric(df["color"])
            if info is None or c is None:
                line["color"] = df["color"].iloc[0]
        return [
            go.Scatter(
                x=x,
                y=y,
                mode="lines",
                line=line,
                opacity=float(df["alpha"].iloc[0]) if "alpha" in df.columns else None,
                showlegend=False,
            )
        ]


def geom_density(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomDensity:
    mapping = mapping if mapping is not None else aes()
    g = GeomDensity(mapping=mapping, data=data)
    g.stat = stat_density()
    g.params.update(kwargs)
    return g
