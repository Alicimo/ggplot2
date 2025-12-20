from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd

from .exceptions import PlotAddError
from .mapping.aes import aes


@dataclass(frozen=True)
class annotate:
    """Annotate helper.

    Minimal support for text annotations via `geom_text`.
    """

    geom: str
    kwargs: dict[str, Any]

    def __radd__(self, other):
        if not hasattr(other, "layers"):
            raise PlotAddError(f"Cannot add annotate to {type(other)!r}")

        if self.geom == "text":
            from .geoms.geom_text import geom_text

            mapping = aes(
                x=self.kwargs.get("x"),
                y=self.kwargs.get("y"),
                label=self.kwargs.get("label"),
            )
            df = pd.DataFrame(
                {
                    "x": [self.kwargs.get("x")],
                    "y": [self.kwargs.get("y")],
                    "label": [self.kwargs.get("label")],
                }
            )
            return other + geom_text(mapping=mapping, data=df)

        # Other geoms could be added later.
        return other


def annotation_logticks(*args: Any, **kwargs: Any):
    # Placeholder (Plotly supports log axes directly).
    return annotate("logticks", {"args": args, **kwargs})


def annotation_stripes(*args: Any, **kwargs: Any):
    # Placeholder.
    return annotate("stripes", {"args": args, **kwargs})
