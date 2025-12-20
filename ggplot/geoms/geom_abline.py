from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomABLine(geom):
    def to_traces(self, df, *, plot):
        # expects intercept and slope
        if "intercept" not in df.columns or "slope" not in df.columns:
            return []

        shapes = []
        # For now, use current x-axis range if available, else [0,1]
        x0, x1 = 0.0, 1.0
        try:
            if hasattr(plot, "scales"):
                for s in plot.scales:
                    if getattr(s, "aesthetic", None) == "x" and hasattr(s, "train"):
                        # fallback: later scale application sets range
                        pass
        except Exception:
            pass

        for _, row in df.iterrows():
            b = float(row["intercept"])
            m = float(row["slope"])
            y0 = m * x0 + b
            y1 = m * x1 + b
            if np.isfinite(y0) and np.isfinite(y1):
                shapes.append(
                    {
                        "type": "line",
                        "x0": x0,
                        "x1": x1,
                        "y0": y0,
                        "y1": y1,
                        "xref": "x",
                        "yref": "y",
                        "line": {"color": "black"},
                    }
                )

        if not hasattr(plot, "_shapes"):
            plot._shapes = []
        plot._shapes.extend(shapes)
        return []


def geom_abline(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomABLine:
    mapping = mapping if mapping is not None else aes()
    g = GeomABLine(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
