from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatDensity2D(stat):
    def __init__(self, n: int = 80):
        self.n = int(n)

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_density_2d requires x and y")

        x = pd.to_numeric(df["x"], errors="coerce").to_numpy(dtype=float)
        y = pd.to_numeric(df["y"], errors="coerce").to_numpy(dtype=float)
        mask = np.isfinite(x) & np.isfinite(y)
        x = x[mask]
        y = y[mask]
        if x.size < 3:
            return pd.DataFrame({"x": [], "y": [], "group": []})

        # Very small 2D KDE and extract one contour-like polyline at a fixed level.
        xmin, xmax = float(x.min()), float(x.max())
        ymin, ymax = float(y.min()), float(y.max())
        gx = np.linspace(xmin, xmax, self.n)
        gy = np.linspace(ymin, ymax, self.n)
        X, Y = np.meshgrid(gx, gy, indexing="xy")

        sx = float(np.std(x))
        sy = float(np.std(y))
        bwx = sx * (x.size ** (-1 / 6)) if sx > 0 else 1.0
        bwy = sy * (y.size ** (-1 / 6)) if sy > 0 else 1.0
        bwx = max(bwx, 1e-9)
        bwy = max(bwy, 1e-9)

        dx = (X[:, :, None] - x[None, None, :]) / bwx
        dy = (Y[:, :, None] - y[None, None, :]) / bwy
        dens = np.exp(-0.5 * (dx**2 + dy**2)).sum(axis=2) / (
            x.size * bwx * bwy * 2 * np.pi
        )

        level = float(np.quantile(dens, 0.9))
        mask = dens >= level
        if not mask.any():
            return pd.DataFrame({"x": [], "y": [], "group": []})

        pts = np.column_stack([X[mask], Y[mask]])
        # Order points by angle around centroid to form a crude contour loop.
        center = pts.mean(axis=0)
        ang = np.arctan2(pts[:, 1] - center[1], pts[:, 0] - center[0])
        order = np.argsort(ang, kind="stable")
        pts = pts[order]

        out = pd.DataFrame({"x": pts[:, 0], "y": pts[:, 1]})
        out["group"] = 1
        return out


def stat_density_2d(*, n: int = 80) -> StatDensity2D:
    return StatDensity2D(n=n)
