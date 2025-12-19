from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import numpy as np
import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomDotplot(geom):
    def to_traces(self, df, *, plot):
        # Minimal: draw points with optional binning along x.
        if "x" not in df.columns:
            return []
        x = df["x"]
        y = df["y"] if "y" in df.columns else np.zeros(len(df))
        return [go.Scatter(x=x, y=y, mode="markers", showlegend=False)]


def geom_dotplot(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any) -> GeomDotplot:
    mapping = mapping if mapping is not None else aes()
    g = GeomDotplot(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g

