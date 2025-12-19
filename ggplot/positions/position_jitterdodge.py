from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .position import position


@dataclass
class position_jitterdodge(position):
    jitter_width: float = 0.1
    jitter_height: float = 0.0
    dodge_width: float = 0.9
    seed: int = 0
    dodge_aesthetic: str = "fill"

    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        rng = np.random.default_rng(self.seed)

        # Dodge
        if "x" in out.columns and self.dodge_aesthetic in out.columns:
            x_codes, x_uniques = pd.factorize(out["x"], sort=False)
            g_codes, g_uniques = pd.factorize(out[self.dodge_aesthetic], sort=False)
            n = max(len(g_uniques), 1)
            offsets = (g_codes - (n - 1) / 2) * (self.dodge_width / n)
            try:
                out["x"] = x_codes.astype(float) + offsets
            except Exception:
                pass

        # Jitter
        if "x" in out.columns:
            try:
                out["x"] = out["x"].astype(float) + rng.uniform(-self.jitter_width, self.jitter_width, size=len(out))
            except Exception:
                pass
        if "y" in out.columns and self.jitter_height:
            try:
                out["y"] = out["y"].astype(float) + rng.uniform(-self.jitter_height, self.jitter_height, size=len(out))
            except Exception:
                pass

        return out

