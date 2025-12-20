from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..mapping.aes import aes
from .geom_raster import GeomRaster, geom_raster


@dataclass
class GeomBin2d(GeomRaster):
    """2D binned heatmap.

    Minimal implementation: expects data already binned with x/y on a grid and
    a `fill` column giving counts/density.
    """


def geom_bin_2d(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomBin2d:
    # Alias to geom_raster until stat_bin_2d is implemented.
    return geom_raster(mapping=mapping, data=data, **kwargs)  # type: ignore[return-value]


def geom_bin2d(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomBin2d:
    return geom_bin_2d(mapping=mapping, data=data, **kwargs)
