from __future__ import annotations

import numpy as np
import pandas as pd

from ..exceptions import GGPlotError
from .stat import stat


class stat_boxplot(stat):
    """Compute boxplot statistics.

    Produces columns: ymin, lower, middle, upper, ymax.
    """

    def compute(self, df: pd.DataFrame, *, mapping):
        if "y" not in df.columns:
            raise GGPlotError("stat_boxplot requires y")

        if "x" in df.columns:
            groups = df.groupby("x", dropna=False, sort=False)
            rows = []
            for xval, sub in groups:
                y = pd.to_numeric(sub["y"], errors="coerce").dropna().to_numpy()
                if y.size == 0:
                    continue
                q1, q2, q3 = np.quantile(y, [0.25, 0.5, 0.75])
                rows.append(
                    {
                        "x": xval,
                        "ymin": float(np.min(y)),
                        "lower": float(q1),
                        "middle": float(q2),
                        "upper": float(q3),
                        "ymax": float(np.max(y)),
                    }
                )
            return pd.DataFrame(rows)

        y = pd.to_numeric(df["y"], errors="coerce").dropna().to_numpy()
        if y.size == 0:
            return pd.DataFrame(
                {"ymin": [], "lower": [], "middle": [], "upper": [], "ymax": []}
            )
        q1, q2, q3 = np.quantile(y, [0.25, 0.5, 0.75])
        return pd.DataFrame(
            {
                "ymin": [float(np.min(y))],
                "lower": [float(q1)],
                "middle": [float(q2)],
                "upper": [float(q3)],
                "ymax": [float(np.max(y))],
            }
        )
