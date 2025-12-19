from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .position import position


@dataclass
class position_dodge(position):
    width: float = 0.9

    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        if "x" not in out.columns:
            return out

        if "fill" not in out.columns:
            return out

        # Map x to integer positions, then offset by category index.
        x_vals = out["x"]
        x_codes, x_uniques = pd.factorize(x_vals, sort=False)
        g_codes, g_uniques = pd.factorize(out["fill"], sort=False)
        n = max(len(g_uniques), 1)

        # Offsets in [-width/2, width/2]
        offsets = (g_codes - (n - 1) / 2) * (self.width / n)
        out["x"] = x_codes.astype(float) + offsets
        return out
