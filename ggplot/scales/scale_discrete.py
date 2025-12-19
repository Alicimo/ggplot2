from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional


@dataclass
class scale_discrete:
    aesthetic: str
    values: Optional[Mapping[Any, Any]] = None

    def __radd__(self, other):
        if not hasattr(other, "scales"):
            other.scales = []
        other.scales.append(self)
        return other

    def map(self, series):
        if self.values is None:
            return series
        return series.map(self.values)


def scale_color_manual(values: Mapping[Any, Any]) -> scale_discrete:
    return scale_discrete(aesthetic="color", values=values)


def scale_colour_manual(values: Mapping[Any, Any]) -> scale_discrete:
    return scale_color_manual(values)


def scale_fill_manual(values: Mapping[Any, Any]) -> scale_discrete:
    return scale_discrete(aesthetic="fill", values=values)
