from __future__ import annotations

import pandas as pd

from .position_stack import position_stack


class position_fill(position_stack):
    """Stack and then rescale to proportions per x.

    Minimal implementation: expects position_stack has created ymin/ymax.
    """

    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        out = super().adjust(df)
        if "x" not in out.columns or "ymax" not in out.columns:
            return out

        for _xval, idx in out.groupby("x", sort=False).groups.items():
            sub = out.loc[list(idx)]
            total = float(sub["ymax"].max()) if len(sub) else 0.0
            if total == 0.0:
                continue
            out.loc[list(idx), "ymin"] = sub["ymin"] / total
            out.loc[list(idx), "ymax"] = sub["ymax"] / total
        return out
