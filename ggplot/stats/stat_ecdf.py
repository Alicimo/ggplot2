from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatECDF(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns:
            raise GGPlotError("stat_ecdf requires x")
        x = pd.to_numeric(df["x"], errors="coerce").dropna().to_numpy(dtype=float)
        if x.size == 0:
            return pd.DataFrame({"x": [], "y": []})
        x = np.sort(x)
        y = np.arange(1, x.size + 1, dtype=float) / float(x.size)
        return pd.DataFrame({"x": x, "y": y})


def stat_ecdf() -> StatECDF:
    return StatECDF()
