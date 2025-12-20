from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomRaster(geom):
    def to_traces(self, df, *, plot):
        # Minimal implementation: treat as a heatmap of z (fill) values.
        # This does not attempt to reproduce pixel-perfect rasterization.
        needed = {"x", "y"}
        if not needed.issubset(df.columns):
            return []
        zcol = "fill" if "fill" in df.columns else "z" if "z" in df.columns else None
        if zcol is None:
            return []

        # Keep categorical axes stable.
        xvals = list(dict.fromkeys(df["x"].tolist()))
        yvals = list(dict.fromkeys(df["y"].tolist()))

        pivot = df.pivot_table(index="y", columns="x", values=zcol, aggfunc="first")
        pivot = pivot.reindex(index=yvals, columns=xvals)

        trace = go.Heatmap(
            x=pivot.columns.tolist(), y=pivot.index.tolist(), z=pivot.values
        )
        if hasattr(plot, "_continuous_scales"):
            info = plot._continuous_scales.get("fill")
            if info is not None:
                trace.update(
                    colorscale=info.get("palette") or "Viridis",
                    zmin=info["domain"][0],
                    zmax=info["domain"][1],
                    showscale=True,
                )
        return [trace]


def geom_raster(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomRaster:
    mapping = mapping if mapping is not None else aes()
    g = GeomRaster(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
