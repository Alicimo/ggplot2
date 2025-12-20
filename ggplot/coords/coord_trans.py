from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from .coord import coord


@dataclass
class CoordTrans(coord):
    xtrans: Callable | None = None
    ytrans: Callable | None = None


def coord_trans(xtrans=None, ytrans=None):
    return CoordTrans(xtrans=xtrans, ytrans=ytrans)
