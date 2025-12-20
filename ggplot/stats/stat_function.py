from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class StatFunction(stat):
    def __init__(self, fun, n: int = 101, args=None):
        self.fun = fun
        self.n = int(n)
        self.args = tuple(args) if args is not None else ()

    def compute(self, df: pd.DataFrame, *, mapping):
        if self.fun is None:
            raise GGPlotError("stat_function requires fun")

        # Determine range: use x if present else [0,1].
        if "x" in df.columns:
            x = pd.to_numeric(df["x"], errors="coerce").dropna().to_numpy(dtype=float)
            xmin, xmax = (0.0, 1.0) if x.size == 0 else (float(x.min()), float(x.max()))
        else:
            xmin, xmax = (0.0, 1.0)
        xs = np.linspace(xmin, xmax, self.n)
        ys = np.array([self.fun(float(v), *self.args) for v in xs], dtype=float)
        return pd.DataFrame({"x": xs, "y": ys})


def stat_function(*, fun, n: int = 101, args=None) -> StatFunction:
    return StatFunction(fun=fun, n=n, args=args)
