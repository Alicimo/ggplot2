from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..exceptions import PlotAddError
from ..geoms.geom_point import GeomPoint
from ..geoms.geom_pointrange import GeomPointrange
from ..layer import layer
from ..mapping.aes import aes
from ..positions.position_identity import position_identity
from .stat_summary import stat_summary as StatSummary
from .stat_summary_range import stat_summary_range as StatSummaryRange


@dataclass
class stat_summary_addable:
    mapping: aes
    data: Any | None = None
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
    data: Any | None = None

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


def stat_summary(
    mapping: aes | None = None, data: Any | None = None, *, fun: str = "mean"
):
    return stat_summary_addable(
        mapping if mapping is not None else aes(), data=data, fun=fun
    )


def stat_summary_range(mapping: aes | None = None, data: Any | None = None):
    return stat_summary_range_addable(
        mapping if mapping is not None else aes(), data=data
    )


def stat_identity():
    from .stat_identity import stat_identity as _stat

    return _stat()


def stat_count():
    from .stat_count import stat_count as _stat

    return _stat()


def stat_bin(*, bins: int = 30):
    from .stat_bin import stat_bin as _stat

    return _stat(bins=bins)


def stat_boxplot():
    from .stat_boxplot import stat_boxplot as _stat

    return _stat()


def stat_density(*, n: int = 100):
    from .stat_density import stat_density as _stat

    return _stat(n=n)


def stat_smooth(*, method: str = "linear"):
    from .stat_smooth import stat_smooth as _stat

    return _stat(method=method)


def stat_quantile(*, quantiles: tuple[float, ...] = (0.5,), n: int = 100):
    from .stat_quantile import stat_quantile as _stat

    return _stat(quantiles=quantiles, n=n)
