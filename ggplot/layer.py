from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

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
    data: Any | None = None
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

    def resolve_after_stat(
        self,
        df: pd.DataFrame,
        *,
        plot_mapping: aes,
        env: Mapping[str, Any] | None = None,
    ) -> pd.DataFrame:
        mapping = aes(**plot_mapping) if self.inherit_aes else aes()
        mapping.update(self.mapping)
        out = df.copy()
        for aes_name, value in mapping.items():
            # Only resolve mappings that are explicitly after_stat(...) here.
            if isinstance(value, after_stat):
                out[aes_name] = evaluate_mapping_value(value.expr, out, env=env)
        return out
