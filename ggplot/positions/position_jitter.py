from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .position import position


@dataclass
class position_jitter(position):
    width: float = 0.1
    height: float = 0.1
    seed: int = 0

    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        rng = np.random.default_rng(self.seed)
        if "x" in out.columns:
            try:
                out["x"] = pd.to_numeric(out["x"], errors="raise").astype(
                    float
                ) + rng.uniform(-self.width, self.width, size=len(out))
            except Exception:
                pass
        if "y" in out.columns:
            try:
                out["y"] = out["y"].astype(float) + rng.uniform(
                    -self.height, self.height, size=len(out)
                )
            except Exception:
                pass
        return out
