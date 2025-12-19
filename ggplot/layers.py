from __future__ import annotations

from collections.abc import Iterable


class Layers(list):
    """Container for layers.

Phase 0: list subclass used by ggplot for + operator wiring.
"""

    def __iadd__(self, other):
        if isinstance(other, Iterable) and not isinstance(other, (str, bytes)):
            self.extend(other)
        else:
            self.append(other)
        return self

