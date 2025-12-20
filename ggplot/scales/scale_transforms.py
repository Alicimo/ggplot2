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
