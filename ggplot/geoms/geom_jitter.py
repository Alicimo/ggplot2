from __future__ import annotations

from typing import Any, Optional

from ..mapping.aes import aes
from ..positions.position_jitter import position_jitter
from .geom_point import geom_point


def geom_jitter(
    mapping: Optional[aes] = None,
    data: Optional[Any] = None,
    *,
    width: float = 0.1,
    height: float = 0.1,
    seed: int = 0,
    **kwargs: Any,
):
    """Convenience wrapper around geom_point(position=position_jitter(...))."""

    return geom_point(
        mapping=mapping,
        data=data,
        position=position_jitter(width=width, height=height, seed=seed),
        **kwargs,
    )

