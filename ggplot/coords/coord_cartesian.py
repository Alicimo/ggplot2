from __future__ import annotations

from dataclasses import dataclass

from .coord import coord


@dataclass
class CoordCartesian(coord):
    pass


def coord_cartesian():
    return CoordCartesian()
