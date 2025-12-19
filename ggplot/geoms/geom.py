from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from ..exceptions import PlotAddError
from ..layer import layer
from ..mapping.aes import aes
from ..positions.position_identity import position_identity
from ..stats.stat_identity import stat_identity


@dataclass
class geom:
    """Base geom.

    Base geom that creates a `layer` when added to a plot.
    """

    mapping: aes = field(default_factory=aes)
    data: Optional[Any] = None
    inherit_aes: bool = True
    show_legend: bool | dict[str, bool] | None = None
    stat: Any = field(default_factory=stat_identity)
    position: Any = field(default_factory=position_identity)
    params: dict[str, Any] = field(default_factory=dict)

    def __radd__(self, other):
        if not hasattr(other, "layers"):
            raise PlotAddError(f"Cannot add geom to {type(other)!r}")
        other.layers.append(
            layer(
                geom=self,
                stat=self.stat,
                position=self.position,
                mapping=self.mapping,
                data=self.data,
                inherit_aes=self.inherit_aes,
                show_legend=self.show_legend,
            )
        )
        return other
