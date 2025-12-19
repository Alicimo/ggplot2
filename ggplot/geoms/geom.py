from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from ..exceptions import PlotAddError
from ..mapping.aes import aes


@dataclass
class geom:
    """Base geom.

    Phase 0: acts as a layer-addable placeholder. In later phases this becomes
    a proper layer factory (geom + stat + position).
    """

    mapping: aes = field(default_factory=aes)
    data: Optional[Any] = None
    inherit_aes: bool = True
    show_legend: bool | dict[str, bool] | None = None

    def __radd__(self, other):
        if not hasattr(other, "layers"):
            raise PlotAddError(f"Cannot add geom to {type(other)!r}")
        other.layers.append(self)
        return other

