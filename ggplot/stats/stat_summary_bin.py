from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatSummaryBin(stat):
    def __init__(self, bins: int = 30, fun: str = "mean"):
        self.bins = int(bins)
        self.fun = str(fun)

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_summary_bin requires x and y")

        x = pd.to_numeric(df["x"], errors="coerce")
        y = pd.to_numeric(df["y"], errors="coerce")
        mask = x.notna() & y.notna()
        x = x[mask].to_numpy(dtype=float)
        y = y[mask].to_numpy(dtype=float)
        if x.size == 0:
            return pd.DataFrame({"x": [], "y": []})

        edges = np.histogram_bin_edges(x, bins=self.bins)
        bin_idx = np.digitize(x, edges, right=False) - 1
        bin_idx = np.clip(bin_idx, 0, len(edges) - 2)

        rows = []
        for b in range(len(edges) - 1):
            ys = y[bin_idx == b]
            if ys.size == 0:
                continue
            mid = float((edges[b] + edges[b + 1]) / 2)
            if self.fun == "mean":
                val = float(np.mean(ys))
            elif self.fun == "median":
                val = float(np.median(ys))
            else:
                raise GGPlotError(f"Unsupported fun for stat_summary_bin: {self.fun!r}")
            rows.append(
                {
                    "x": mid,
                    "y": val,
                    "xmin": float(edges[b]),
                    "xmax": float(edges[b + 1]),
                }
            )
        return pd.DataFrame(rows)


def stat_summary_bin(*, bins: int = 30, fun: str = "mean") -> StatSummaryBin:
    return StatSummaryBin(bins=bins, fun=fun)
