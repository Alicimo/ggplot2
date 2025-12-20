from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


def _convex_hull(points: np.ndarray) -> np.ndarray:
    # Monotonic chain convex hull. Points shape (n,2).
    pts = points[np.lexsort((points[:, 1], points[:, 0]))]

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(tuple(p))

    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(tuple(p))

    hull = lower[:-1] + upper[:-1]
    return np.array(hull, dtype=float)


class StatHull(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_hull requires x and y")
        x = pd.to_numeric(df["x"], errors="coerce").to_numpy(dtype=float)
        y = pd.to_numeric(df["y"], errors="coerce").to_numpy(dtype=float)
        mask = np.isfinite(x) & np.isfinite(y)
        pts = np.column_stack([x[mask], y[mask]])
        if pts.shape[0] < 3:
            return pd.DataFrame({"x": [], "y": [], "group": []})

        hull = _convex_hull(pts)
        out = pd.DataFrame({"x": hull[:, 0], "y": hull[:, 1]})
        out["group"] = 1
        return out


def stat_hull() -> StatHull:
    return StatHull()
