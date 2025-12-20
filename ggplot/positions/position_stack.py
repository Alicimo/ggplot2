from __future__ import annotations

import pandas as pd

from .position import position


class position_stack(position):
    """Stack bars by cumulative sum within x.

    Expects a column named `y` (or `count`) and an optional `fill` grouping.
    Produces `ymin`/`ymax` for bar rendering.
    """

    def adjust(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        ycol = (
            "y" if "y" in out.columns else "count" if "count" in out.columns else None
        )
        if ycol is None or "x" not in out.columns:
            return out

        group_cols = ["x"]
        if "fill" in out.columns:
            group_cols.append("fill")

        # Ensure stable order: preserve input order within each x.
        out["_row"] = range(len(out))
        out = out.sort_values(["x", "_row"], kind="stable")

        out["ymin"] = 0.0
        out["ymax"] = 0.0
        for _xval, sub_idx in out.groupby("x", sort=False).groups.items():
            idx = list(sub_idx)
            sub = out.loc[idx]
            y = pd.to_numeric(sub[ycol], errors="coerce").fillna(0)
            csum = y.cumsum()
            out.loc[idx, "ymax"] = csum.values
            out.loc[idx, "ymin"] = (csum - y).values
        out = out.drop(columns=["_row"])
        return out
