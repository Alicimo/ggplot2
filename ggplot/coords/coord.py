from __future__ import annotations

from dataclasses import dataclass


@dataclass
class coord:
    def __radd__(self, other):
        other.coord = self
        return other

