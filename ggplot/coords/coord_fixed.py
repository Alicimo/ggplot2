from __future__ import annotations

from dataclasses import dataclass

from .coord import coord


@dataclass
class CoordFixed(coord):
    ratio: float = 1.0


def coord_fixed(ratio: float = 1.0):
    return CoordFixed(ratio=ratio)
