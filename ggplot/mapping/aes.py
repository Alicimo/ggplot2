from __future__ import annotations

from typing import Any

from ..exceptions import MappingError


class aes(dict[str, Any]):
    """Aesthetic mappings.

Phase 0: a thin dict-like container. We add evaluation/expression support in
later phases.
"""

    def __init__(self, x: Any = None, y: Any = None, **kwargs: Any):
        if x is not None:
            kwargs["x"] = x
        if y is not None:
            kwargs["y"] = y

        for key in kwargs:
            if not isinstance(key, str) or not key:
                raise MappingError(f"Invalid aesthetic name: {key!r}")

        super().__init__(kwargs)

