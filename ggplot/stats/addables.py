from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from ..exceptions import PlotAddError
from ..layer import layer
from ..mapping.aes import aes
from ..positions.position_identity import position_identity
from ..geoms.geom_point import GeomPoint
from ..geoms.geom_pointrange import GeomPointrange
from .stat_summary import stat_summary as StatSummary
from .stat_summary_range import stat_summary_range as StatSummaryRange


@dataclass
class stat_summary_addable:
    mapping: aes
    data: Optional[Any] = None
    fun: str = "mean"

    def __radd__(self, other):
        if not hasattr(other, "layers"):
            raise PlotAddError(f"Cannot add stat_summary to {type(other)!r}")
        other.layers.append(
            layer(
                geom=GeomPoint(),
                stat=StatSummary(fun=self.fun),
                position=position_identity(),
                mapping=self.mapping,
                data=self.data,
            )
        )
        return other


@dataclass
class stat_summary_range_addable:
    mapping: aes
    data: Optional[Any] = None

    def __radd__(self, other):
        if not hasattr(other, "layers"):
            raise PlotAddError(f"Cannot add stat_summary_range to {type(other)!r}")
        other.layers.append(
            layer(
                geom=GeomPointrange(),
                stat=StatSummaryRange(),
                position=position_identity(),
                mapping=self.mapping,
                data=self.data,
            )
        )
        return other


def stat_summary(mapping: Optional[aes] = None, data: Optional[Any] = None, *, fun: str = "mean"):
    return stat_summary_addable(mapping if mapping is not None else aes(), data=data, fun=fun)


def stat_summary_range(mapping: Optional[aes] = None, data: Optional[Any] = None):
    return stat_summary_range_addable(mapping if mapping is not None else aes(), data=data)

