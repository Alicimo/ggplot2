from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass
class scale_position_discrete:
    aesthetic: str
    limits: Sequence[str] | None = None

    def __radd__(self, other):
        if not hasattr(other, "scales"):
            other.scales = []
        other.scales.append(self)
        return other


def scale_x_discrete(*, limits=None) -> scale_position_discrete:
    return scale_position_discrete(aesthetic="x", limits=limits)


def scale_y_discrete(*, limits=None) -> scale_position_discrete:
    return scale_position_discrete(aesthetic="y", limits=limits)
