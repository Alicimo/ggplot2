from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..mapping.aes import aes
from ..stats.stat_quantile import stat_quantile
from .geom_line import GeomLine


@dataclass
class GeomQuantile(GeomLine):
    def __post_init__(self):
        if self.stat is None:
            self.stat = stat_quantile()


def geom_quantile(
    mapping: aes | None = None, data: Any | None = None, **kwargs: Any
) -> GeomQuantile:
    mapping = mapping if mapping is not None else aes()
    g = GeomQuantile(mapping=mapping, data=data)
    g.stat = stat_quantile()
    g.params.update(kwargs)
    return g
