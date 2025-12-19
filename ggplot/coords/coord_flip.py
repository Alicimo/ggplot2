from __future__ import annotations

from dataclasses import dataclass

from .coord import coord


@dataclass
class CoordFlip(coord):
    pass


def coord_flip():
    return CoordFlip()

