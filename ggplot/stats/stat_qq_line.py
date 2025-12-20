from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatQQLine(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        sample_col = (
            "sample" if "sample" in df.columns else "y" if "y" in df.columns else None
        )
        if sample_col is None:
            raise GGPlotError("stat_qq_line requires `sample` or `y`")

        sample = (
            pd.to_numeric(df[sample_col], errors="coerce")
            .dropna()
            .to_numpy(dtype=float)
        )
        if sample.size < 2:
            return pd.DataFrame({"x": [], "y": []})

        sample = np.sort(sample)
        p = (np.arange(1, sample.size + 1) - 0.5) / sample.size
        from statistics import NormalDist

        theo = np.array([NormalDist().inv_cdf(float(pi)) for pi in p], dtype=float)

        qx = np.quantile(theo, [0.25, 0.75])
        qy = np.quantile(sample, [0.25, 0.75])
        if float(qx[1] - qx[0]) == 0.0:
            return pd.DataFrame({"x": [], "y": []})
        slope = float((qy[1] - qy[0]) / (qx[1] - qx[0]))
        intercept = float(qy[0] - slope * qx[0])

        xline = np.array([theo.min(), theo.max()], dtype=float)
        yline = slope * xline + intercept
        return pd.DataFrame({"x": xline, "y": yline})


def stat_qq_line() -> StatQQLine:
    return StatQQLine()
