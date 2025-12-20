from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass

import numpy as np

from .scale import scale


@dataclass
class scale_position_continuous(scale):
    limits: tuple[float, float] | None = None
    breaks: Sequence[float] | None = None

    def train(self, values) -> tuple[float, float]:
        arr = np.asarray(values, dtype=float)
        arr = arr[np.isfinite(arr)]
        if self.limits is not None:
            return self.limits
        if arr.size == 0:
            return (0.0, 1.0)
        return (float(arr.min()), float(arr.max()))


def scale_x_continuous(*, limits=None, breaks=None) -> scale_position_continuous:
    return scale_position_continuous(aesthetic="x", limits=limits, breaks=breaks)


def scale_y_continuous(*, limits=None, breaks=None) -> scale_position_continuous:
    return scale_position_continuous(aesthetic="y", limits=limits, breaks=breaks)
