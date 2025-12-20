from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .exceptions import PlotAddError


@dataclass(frozen=True)
class labs:
    """Labels addable.

    Phase 0: stores labels on the plot object under `plot.labels`.
    """

    title: str | None = None
    x: str | None = None
    y: str | None = None
    caption: str | None = None

    def __radd__(self, other):
        if not hasattr(other, "__dict__"):
            raise PlotAddError(f"Cannot add labs to {type(other)!r}")
        labels = getattr(other, "labels", None)
        if labels is None:
            other.labels = {}
            labels = other.labels
        for key, value in (
            ("title", self.title),
            ("x", self.x),
            ("y", self.y),
            ("caption", self.caption),
        ):
            if value is not None:
                labels[key] = value
        return other


class theme:
    """Backwards-compatible theme addable.

    Prefer importing `theme` from `ggplot.themes` going forward.
    """

    def __init__(self, **kwargs: Any):
        self.kwargs = dict(kwargs)

    def __radd__(self, other):
        if not hasattr(other, "__dict__"):
            raise PlotAddError(f"Cannot add theme to {type(other)!r}")
        current = getattr(other, "theme", None)
        if current is None:
            other.theme = {}
            current = other.theme
        current.update(self.kwargs)
        return other
