from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class stat_density(stat):
    """A very small kernel density estimate.

    This is a minimal implementation intended for violin and density-like plots.
    It does not aim for full plotnine parity.
    """

    def __init__(self, n: int = 256, bw: float | None = None):
        self.n = n
        self.bw = bw

    def compute(self, df: pd.DataFrame, *, mapping):
        if "y" not in df.columns:
            raise GGPlotError("stat_density requires y")

        y = pd.to_numeric(df["y"], errors="coerce").dropna().to_numpy()
        if y.size == 0:
            return pd.DataFrame({"y": [], "density": []})

        ymin = float(np.min(y))
        ymax = float(np.max(y))
        grid = np.linspace(ymin, ymax, int(self.n))

        if self.bw is None:
            # Scott's rule of thumb
            std = float(np.std(y))
            bw = std * (y.size ** (-1 / 5)) if std > 0 else 1.0
        else:
            bw = float(self.bw)
        bw = max(bw, 1e-9)

        # Gaussian KDE
        diffs = (grid[:, None] - y[None, :]) / bw
        dens = np.exp(-0.5 * diffs**2).sum(axis=1) / (y.size * bw * np.sqrt(2 * np.pi))
        out = pd.DataFrame({"y": grid, "density": dens})
        if "x" in df.columns:
            out["x"] = df["x"].iloc[0]
        return out

