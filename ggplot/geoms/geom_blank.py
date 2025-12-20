from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..mapping.aes import aes
from .geom import geom


@dataclass
class GeomBlank(geom):
    def to_traces(self, df, *, plot):
        # Intentionally draws nothing.
        return []


def geom_blank(mapping: aes | None = None, data: Any | None = None, **kwargs: Any):
    mapping = mapping if mapping is not None else aes()
    g = GeomBlank(mapping=mapping, data=data)
    g.params.update(kwargs)
    return g
