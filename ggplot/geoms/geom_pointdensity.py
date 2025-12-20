from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomPointdensity(geom):
    def to_traces(self, df, *, plot):
        # Minimal: compute a crude local density proxy and map to marker color.
        if "x" not in df.columns or "y" not in df.columns:
            return []
        x = df["x"].to_numpy(dtype=float)
        y = df["y"].to_numpy(dtype=float)
        if x.size == 0:
            return []

        # Simple density proxy: inverse mean distance to k nearest neighbors.
        k = int(self.params.get("k", 5))
        k = max(1, min(k, x.size - 1))
        if x.size < 2:
            dens = np.ones_like(x, dtype=float)
        else:
            pts = np.column_stack([x, y])
            d2 = ((pts[:, None, :] - pts[None, :, :]) ** 2).sum(axis=2)
            np.fill_diagonal(d2, np.inf)
            kth = np.partition(d2, k - 1, axis=1)[:, k - 1]
            dens = 1.0 / np.sqrt(kth)
            dens[np.isinf(dens)] = 0.0

        marker = {"color": dens, "colorscale": "Viridis", "showscale": True}
        return [go.Scatter(x=x, y=y, mode="markers", marker=marker, showlegend=False)]


def geom_pointdensity(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomPointdensity:
    mapping = mapping if mapping is not None else aes()
    g = GeomPointdensity(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
