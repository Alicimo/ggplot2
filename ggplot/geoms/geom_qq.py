from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np
import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomQQ(geom):
    def to_traces(self, df, *, plot):
        # Minimal: expects `sample` column (as in plotnine) or uses `y`.
        sample_col = (
            "sample" if "sample" in df.columns else "y" if "y" in df.columns else None
        )
        if sample_col is None:
            return []

        sample = df[sample_col].dropna().to_numpy(dtype=float)
        if sample.size == 0:
            return []

        sample = np.sort(sample)
        # Standard normal theoretical quantiles.
        p = (np.arange(1, sample.size + 1) - 0.5) / sample.size
        try:
            from statistics import NormalDist

            theo = np.array([NormalDist().inv_cdf(float(pi)) for pi in p], dtype=float)
        except Exception:
            # Fallback: approximate via numpy if available; otherwise plot sample vs itself.
            theo = sample

        return [go.Scatter(x=theo, y=sample, mode="markers", showlegend=False)]


def geom_qq(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomQQ:
    mapping = mapping if mapping is not None else aes()
    g = GeomQQ(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
