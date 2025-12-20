from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomSina(geom):
    def to_traces(self, df, *, plot):
        # Minimal: jitter x by a small amount and render points.
        if "x" not in df.columns or "y" not in df.columns:
            return []
        width = float(self.params.get("width", 0.4))
        rng = np.random.default_rng(int(self.params.get("seed", 0)))

        x = df["x"].to_numpy(dtype=float)
        y = df["y"].to_numpy(dtype=float)
        x = x + rng.uniform(-width / 2, width / 2, size=x.shape)

        marker = {}
        if "color" in df.columns:
            marker["color"] = df["color"]

        return [go.Scatter(x=x, y=y, mode="markers", marker=marker, showlegend=False)]


def geom_sina(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomSina:
    mapping = mapping if mapping is not None else aes()
    g = GeomSina(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
