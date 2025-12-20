from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomQQLine(geom):
    def to_traces(self, df, *, plot):
        sample_col = (
            "sample" if "sample" in df.columns else "y" if "y" in df.columns else None
        )
        if sample_col is None:
            return []

        sample = df[sample_col].dropna().to_numpy(dtype=float)
        if sample.size < 2:
            return []

        sample = np.sort(sample)
        p = (np.arange(1, sample.size + 1) - 0.5) / sample.size
        from statistics import NormalDist

        theo = np.array([NormalDist().inv_cdf(float(pi)) for pi in p], dtype=float)

        # Fit line through 1st and 3rd quartiles (common QQ reference line).
        qx = np.quantile(theo, [0.25, 0.75])
        qy = np.quantile(sample, [0.25, 0.75])
        if float(qx[1] - qx[0]) == 0.0:
            return []
        slope = float((qy[1] - qy[0]) / (qx[1] - qx[0]))
        intercept = float(qy[0] - slope * qx[0])

        xline = np.array([theo.min(), theo.max()], dtype=float)
        yline = slope * xline + intercept
        return [go.Scatter(x=xline, y=yline, mode="lines", showlegend=False)]


def geom_qq_line(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomQQLine:
    mapping = mapping if mapping is not None else aes()
    g = GeomQQLine(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
