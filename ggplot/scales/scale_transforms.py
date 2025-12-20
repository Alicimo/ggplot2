from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass

import numpy as np

from .scale_xy import scale_position_continuous


@dataclass
class scale_position_transformed(scale_position_continuous):
    transform: Callable[[np.ndarray], np.ndarray] | None = None
    inverse: Callable[[np.ndarray], np.ndarray] | None = None

    def apply(self, values):
        if self.transform is None:
            return values
        arr = np.asarray(values, dtype=float)
        return self.transform(arr)


def scale_x_log10(
    *, limits=None, breaks: Sequence[float] | None = None
) -> scale_position_transformed:
    return scale_position_transformed(
        aesthetic="x",
        limits=limits,
        breaks=breaks,
        transform=lambda a: np.log10(a),
        inverse=lambda a: 10**a,
    )


def scale_y_log10(
    *, limits=None, breaks: Sequence[float] | None = None
) -> scale_position_transformed:
    return scale_position_transformed(
        aesthetic="y",
        limits=limits,
        breaks=breaks,
        transform=lambda a: np.log10(a),
        inverse=lambda a: 10**a,
    )


def scale_x_reverse(*, limits=None, breaks: Sequence[float] | None = None):
    return scale_position_transformed(
        aesthetic="x",
        limits=limits,
        breaks=breaks,
        transform=lambda a: -a,
        inverse=lambda a: -a,
    )


def scale_y_reverse(*, limits=None, breaks: Sequence[float] | None = None):
    return scale_position_transformed(
        aesthetic="y",
        limits=limits,
        breaks=breaks,
        transform=lambda a: -a,
        inverse=lambda a: -a,
    )


def scale_x_sqrt(*, limits=None, breaks: Sequence[float] | None = None):
    return scale_position_transformed(
        aesthetic="x",
        limits=limits,
        breaks=breaks,
        transform=lambda a: np.sqrt(a),
        inverse=lambda a: a**2,
    )


def scale_y_sqrt(*, limits=None, breaks: Sequence[float] | None = None):
    return scale_position_transformed(
        aesthetic="y",
        limits=limits,
        breaks=breaks,
        transform=lambda a: np.sqrt(a),
        inverse=lambda a: a**2,
    )


def scale_x_symlog(*, limits=None, breaks: Sequence[float] | None = None):
    def _symlog(a: np.ndarray) -> np.ndarray:
        return np.sign(a) * np.log1p(np.abs(a))

    def _inv(a: np.ndarray) -> np.ndarray:
        return np.sign(a) * (np.expm1(np.abs(a)))

    return scale_position_transformed(
        aesthetic="x",
        limits=limits,
        breaks=breaks,
        transform=_symlog,
        inverse=_inv,
    )


def scale_y_symlog(*, limits=None, breaks: Sequence[float] | None = None):
    def _symlog(a: np.ndarray) -> np.ndarray:
        return np.sign(a) * np.log1p(np.abs(a))

    def _inv(a: np.ndarray) -> np.ndarray:
        return np.sign(a) * (np.expm1(np.abs(a)))

    return scale_position_transformed(
        aesthetic="y",
        limits=limits,
        breaks=breaks,
        transform=_symlog,
        inverse=_inv,
    )


def scale_x_date(*args, **kwargs):
    # Placeholder (Plotly handles datetimes on axes).
    return scale_position_transformed(aesthetic="x")


def scale_y_date(*args, **kwargs):
    return scale_position_transformed(aesthetic="y")


def scale_x_datetime(*args, **kwargs):
    return scale_position_transformed(aesthetic="x")


def scale_y_datetime(*args, **kwargs):
    return scale_position_transformed(aesthetic="y")


def scale_x_timedelta(*args, **kwargs):
    return scale_position_transformed(aesthetic="x")


def scale_y_timedelta(*args, **kwargs):
    return scale_position_transformed(aesthetic="y")
