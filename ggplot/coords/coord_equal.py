from __future__ import annotations

from dataclasses import dataclass

from .coord_fixed import CoordFixed


@dataclass
class CoordEqual(CoordFixed):
    """Alias for coord_fixed."""


def coord_equal(*, ratio: float = 1.0) -> CoordEqual:
    return CoordEqual(ratio=ratio)
