from __future__ import annotations

from typing import Callable, Literal

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


SummaryFun = Literal["mean", "median"]


class stat_summary(stat):
    def __init__(self, fun: SummaryFun = "mean"):
        self.fun = fun

    def compute(self, df: pd.DataFrame, *, mapping):
        if "x" not in df.columns or "y" not in df.columns:
            raise GGPlotError("stat_summary requires x and y")

        def agg(vals: pd.Series) -> float:
            v = pd.to_numeric(vals, errors="coerce").dropna().to_numpy()
            if v.size == 0:
                return float("nan")
            if self.fun == "mean":
                return float(np.mean(v))
            if self.fun == "median":
                return float(np.median(v))
            raise GGPlotError(f"Unsupported summary fun: {self.fun!r}")

        out = df.groupby("x", dropna=False, sort=False)["y"].apply(agg).reset_index(name="y")
        return out

