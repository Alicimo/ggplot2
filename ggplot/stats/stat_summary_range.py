from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class stat_summary_range(stat):
    """Compute mean and min/max range for y within each x.

    Produces: y (mean), ymin (min), ymax (max)
    """

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_summary_range requires x and y")

        def summarize(vals: pd.Series):
            v = pd.to_numeric(vals, errors="coerce").dropna().to_numpy()
            if v.size == 0:
                return (float("nan"), float("nan"), float("nan"))
            return (float(np.mean(v)), float(np.min(v)), float(np.max(v)))

        rows = []
        for xval, sub in df.groupby("x", dropna=False, sort=False):
            ymean, ymin, ymax = summarize(sub["y"])
            rows.append({"x": xval, "y": ymean, "ymin": ymin, "ymax": ymax})
        return pd.DataFrame(rows)
