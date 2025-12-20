from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .position import position


@dataclass
class position_nudge(position):
    x: float = 0.0
    y: float = 0.0

    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        if "x" in out.columns:
            try:
                out["x"] = out["x"].astype(float) + float(self.x)
            except Exception:
                pass
        if "y" in out.columns:
            try:
                out["y"] = out["y"].astype(float) + float(self.y)
            except Exception:
                pass
        return out
