from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional

import pandas as pd

from ._utils.data import as_data_frame
from .mapping.aes import aes
from .mapping.evaluation import after_stat, evaluate_mapping_value


@dataclass
class layer:
    geom: Any
    stat: Any
    position: Any
    mapping: aes
    data: Optional[Any] = None
    inherit_aes: bool = True
    show_legend: bool | dict[str, bool] | None = None

    def setup_data(self, plot_data: pd.DataFrame) -> pd.DataFrame:
        if self.data is None:
            return plot_data
        return as_data_frame(self.data)

    def resolve_mapping(
        self,
        df: pd.DataFrame,
        *,
        plot_mapping: aes,
        env: Mapping[str, Any] | None = None,
        stage: str = "start",
    ) -> pd.DataFrame:
        mapping = aes(**plot_mapping) if self.inherit_aes else aes()
        mapping.update(self.mapping)

        out = df.copy()
        for aes_name, value in mapping.items():
            resolved = evaluate_mapping_value(value, out, env=env)
            if stage == "start" and isinstance(resolved, after_stat):
                continue
            out[aes_name] = resolved
        return out

