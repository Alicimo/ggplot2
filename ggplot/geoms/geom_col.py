from __future__ import annotations

from typing import Any, Optional

from ..mapping.aes import aes
from .geom_bar import geom_bar


def geom_col(mapping: Optional[aes] = None, data: Optional[Any] = None, **kwargs: Any):
    """Bar chart with heights given by y (identity stat).

    This is a convenience wrapper around geom_bar(stat='identity').
    """

    return geom_bar(mapping=mapping, data=data, stat="identity", **kwargs)

