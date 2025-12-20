from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatQQ(stat):
    def compute(self, df: pd.DataFrame, *, mapping):
        sample_col = (
            "sample" if "sample" in df.columns else "y" if "y" in df.columns else None
        )
        if sample_col is None:
            raise GGPlotError("stat_qq requires `sample` or `y`")

        sample = (
            pd.to_numeric(df[sample_col], errors="coerce")
            .dropna()
            .to_numpy(dtype=float)
        )
        if sample.size == 0:
            return pd.DataFrame({"x": [], "y": []})

        sample = np.sort(sample)
        p = (np.arange(1, sample.size + 1) - 0.5) / sample.size
        from statistics import NormalDist

        theo = np.array([NormalDist().inv_cdf(float(pi)) for pi in p], dtype=float)
        return pd.DataFrame({"x": theo, "y": sample})


def stat_qq() -> StatQQ:
    return StatQQ()
