from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..mapping.aes import aes
from .geom_polygon import GeomPolygon, geom_polygon


@dataclass
class GeomMap(GeomPolygon):
    """Minimal geom_map.

    Plotnine/ggplot2 expect a polygon-like rendering backed by a map dataframe.
    In this Plotly port we treat it as an alias of `geom_polygon`.
    """


def geom_map(mapping: aes | None = None, data: Any | None = None, **kwargs: Any):
    return geom_polygon(mapping=mapping, data=data, **kwargs)  # type: ignore[return-value]
