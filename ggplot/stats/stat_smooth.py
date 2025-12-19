from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class stat_smooth(stat):
    """Minimal smoothing stat.

    v0 implementation: simple linear regression fit producing yhat over sorted x.
    """

    def __init__(self, n: int = 80):
        self.n = n

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_smooth requires x and y")
        x = pd.to_numeric(df["x"], errors="coerce")
        y = pd.to_numeric(df["y"], errors="coerce")
        mask = x.notna() & y.notna()
        x = x[mask].to_numpy(dtype=float)
        y = y[mask].to_numpy(dtype=float)
        if x.size < 2:
            return pd.DataFrame({"x": [], "y": []})

        order = np.argsort(x)
        x = x[order]
        y = y[order]

        # Linear fit
        A = np.vstack([x, np.ones_like(x)]).T
        coef, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
        slope, intercept = float(coef[0]), float(coef[1])

        xs = np.linspace(float(x.min()), float(x.max()), int(self.n))
        ys = slope * xs + intercept
        out = pd.DataFrame({"x": xs, "y": ys})
        return out

