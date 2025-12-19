from __future__ import annotations

from dataclasses import dataclass


@dataclass
class scale:
    aesthetic: str

    def __radd__(self, other):
        if not hasattr(other, "scales"):
            other.scales = []
        other.scales.append(self)
        return other

