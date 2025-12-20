from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatSina(stat):
    def __init__(self, seed: int = 0, width: float = 0.4):
        self.seed = int(seed)
        self.width = float(width)

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_sina requires x and y")
        out = df.copy()
        rng = np.random.default_rng(self.seed)
        x = pd.to_numeric(out["x"], errors="coerce")
        jitter = rng.uniform(-self.width / 2, self.width / 2, size=len(out))
        out["x"] = x + jitter
        return out


def stat_sina(*, seed: int = 0, width: float = 0.4) -> StatSina:
    return StatSina(seed=seed, width=width)
