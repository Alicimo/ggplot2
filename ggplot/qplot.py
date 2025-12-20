from __future__ import annotations

from typing import Any

import pandas as pd

from .geoms.geom_bar import geom_bar
from .geoms.geom_point import geom_point
from .ggplot import ggplot
from .mapping.aes import aes


def qplot(
    x: Any | None = None,
    y: Any | None = None,
    *,
    data: pd.DataFrame | None = None,
    geom: str = "point",
    **kwargs: Any,
):
    """Quick plot helper (very small subset of plotnine.qplot).

    Parameters
    ----------
    x, y:
        Column names or values.
    data:
        DataFrame.
    geom:
        'point' or 'bar' (v0).
    """

    p = ggplot(data, aes(x=x, y=y))
    if geom == "point":
        return p + geom_point(**kwargs)
    if geom == "bar":
        return p + geom_bar(**kwargs)
    raise ValueError(f"Unsupported geom for qplot: {geom!r}")
