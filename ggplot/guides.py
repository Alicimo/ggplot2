from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .exceptions import PlotAddError


@dataclass(frozen=True)
class guides:
    """Stub for guides().

    Plotly handles legends/colorbars differently than ggplot2/plotnine.
    For now we store guide requests on the plot object for potential future
    translation.
    """

    kwargs: dict[str, Any]

    def __radd__(self, other):
        if not hasattr(other, "__dict__"):
            raise PlotAddError(f"Cannot add guides to {type(other)!r}")
        other.guides = dict(self.kwargs)
        return other


def guide_legend(**kwargs: Any) -> dict[str, Any]:
    return {"type": "legend", **kwargs}


def guide_colorbar(**kwargs: Any) -> dict[str, Any]:
    return {"type": "colorbar", **kwargs}


def guide_colourbar(**kwargs: Any) -> dict[str, Any]:
    return guide_colorbar(**kwargs)
