from __future__ import annotations

from typing import Any

import numpy as np


def has_continuous_scale(plot, aesthetic: str) -> bool:
    return bool(getattr(plot, "_continuous_scales", {}).get(aesthetic))


def continuous_scale_info(plot, aesthetic: str) -> dict[str, Any] | None:
    return getattr(plot, "_continuous_scales", {}).get(aesthetic)


def try_as_numeric(values) -> np.ndarray | None:
    try:
        arr = np.asarray(values, dtype=float)
    except Exception:
        return None
    if not np.isfinite(arr).any():
        return None
    return arr
