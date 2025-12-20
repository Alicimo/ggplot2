from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .exceptions import PlotAddError
from .scales.scale_xy import scale_position_continuous
from .scales.scale_xy_discrete import scale_position_discrete


@dataclass(frozen=True)
class lims:
    """Set limits on position scales.

    Minimal implementation: supports x/y with either
    - tuple(min, max) for continuous scales
    - list of categories for discrete scales
    """

    x: Any | None = None
    y: Any | None = None

    def __radd__(self, other):
        if not hasattr(other, "scales"):
            other.scales = []

        if self.x is not None:
            if (
                isinstance(self.x, (list, tuple))
                and len(self.x) > 0
                and isinstance(self.x[0], str)
            ):
                other.scales.append(
                    scale_position_discrete(aesthetic="x", limits=self.x)
                )
            else:
                other.scales.append(
                    scale_position_continuous(aesthetic="x", limits=self.x)
                )

        if self.y is not None:
            if (
                isinstance(self.y, (list, tuple))
                and len(self.y) > 0
                and isinstance(self.y[0], str)
            ):
                other.scales.append(
                    scale_position_discrete(aesthetic="y", limits=self.y)
                )
            else:
                other.scales.append(
                    scale_position_continuous(aesthetic="y", limits=self.y)
                )

        return other


def xlim(*args):
    if len(args) != 2:
        raise ValueError("xlim expects 2 arguments: (min, max)")
    return lims(x=(args[0], args[1]))


def ylim(*args):
    if len(args) != 2:
        raise ValueError("ylim expects 2 arguments: (min, max)")
    return lims(y=(args[0], args[1]))


def expand_limits(**kwargs: Any):
    """Backwards-compatible placeholder.

    In plotnine this expands the axis ranges; here we approximate by setting
    limits if provided.
    """

    if not kwargs:
        raise PlotAddError("expand_limits requires at least one keyword argument")
    return lims(x=kwargs.get("x"), y=kwargs.get("y"))
