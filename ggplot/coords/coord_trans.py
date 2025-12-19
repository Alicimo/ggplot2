from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from .coord import coord


@dataclass
class CoordTrans(coord):
    xtrans: Optional[Callable] = None
    ytrans: Optional[Callable] = None


def coord_trans(xtrans=None, ytrans=None):
    return CoordTrans(xtrans=xtrans, ytrans=ytrans)

