from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatEllipse(stat):
    def __init__(self, n: int = 100):
        self.n = int(n)

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_ellipse requires x and y")
        x = pd.to_numeric(df["x"], errors="coerce").dropna().to_numpy(dtype=float)
        y = pd.to_numeric(df["y"], errors="coerce").dropna().to_numpy(dtype=float)
        if x.size < 3:
            return pd.DataFrame({"x": [], "y": [], "group": []})

        mean = np.array([x.mean(), y.mean()], dtype=float)
        cov = np.cov(np.vstack([x, y]))
        vals, vecs = np.linalg.eigh(cov)
        vals = np.maximum(vals, 1e-12)
        # 1-sigma ellipse
        t = np.linspace(0, 2 * np.pi, self.n)
        circle = np.column_stack([np.cos(t), np.sin(t)])
        scale = np.sqrt(vals)
        ell = circle @ (vecs * scale)
        ell = ell + mean
        out = pd.DataFrame({"x": ell[:, 0], "y": ell[:, 1]})
        out["group"] = 1
        return out


def stat_ellipse(*, n: int = 100) -> StatEllipse:
    return StatEllipse(n=n)
