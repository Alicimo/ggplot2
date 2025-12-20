from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import plotly.graph_objects as go

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomPoint(geom):
    def to_traces(self, df, *, plot):
        if "x" not in df.columns or "y" not in df.columns:
            return []
        if "color" in df.columns:
            # Continuous color mapping: single trace with colorscale.
            try:
                import numpy as np

                col = np.asarray(df["color"], dtype=float)
                if np.isfinite(col).any() and hasattr(plot, "_continuous_scales"):
                    info = plot._continuous_scales.get("color")
                    if info is not None:
                        marker = {
                            "color": col,
                            "colorscale": info.get("palette") or "Viridis",
                            "cmin": info["domain"][0],
                            "cmax": info["domain"][1],
                            "showscale": True,
                        }
                        if "size" in df.columns:
                            marker["size"] = df["size"]
                        return [
                            go.Scatter(
                                x=df["x"],
                                y=df["y"],
                                mode="markers",
                                marker=marker,
                                showlegend=False,
                            )
                        ]
            except Exception:
                # Fall back to discrete handling.
                pass

            traces = []
            for key, sub in df.groupby("color", dropna=False, sort=False):
                marker = {"color": key}
                if "size" in sub.columns:
                    marker["size"] = sub["size"]
                # Prefer original discrete label if present.
                name = (
                    sub["colour"].iloc[0]
                    if "colour" in sub.columns and not sub.empty
                    else key
                )
                traces.append(
                    go.Scatter(
                        x=sub["x"],
                        y=sub["y"],
                        mode="markers",
                        marker=marker,
                        name=str(name),
                    )
                )
            return traces

        marker = {}
        if "size" in df.columns:
            marker["size"] = df["size"]
        return [go.Scatter(x=df["x"], y=df["y"], mode="markers", marker=marker)]


def geom_point(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomPoint:
    mapping = mapping if mapping is not None else aes()
    g = GeomPoint(mapping=mapping, data=data)
    if "position" in kwargs:
        g.position = kwargs.pop("position")
    g.params.update(kwargs)
    return g
