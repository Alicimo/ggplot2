from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class theme:
    params: dict[str, Any]

    def __init__(self, **kwargs: Any):
        self.params = dict(kwargs)

    def __radd__(self, other):
        if not hasattr(other, "theme"):
            other.theme = {}
        other.theme.update(self.params)
        return other

