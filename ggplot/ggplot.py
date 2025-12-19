from __future__ import annotations

from copy import deepcopy
from typing import Any, Optional

import pandas as pd

from ._utils.data import as_data_frame
from .exceptions import PlotAddError
from .layers import Layers
from .mapping.aes import aes
from .typing import DataLike, PlotAddable


class ggplot:
    """Create a new ggplot object.

    Phase 0: stores data + mapping and supports the additive API.
    Rendering/build pipeline is added in later phases.
    """

    def __init__(self, data: Optional[DataLike] = None, mapping: Optional[aes] = None):
        self.data: pd.DataFrame = as_data_frame(data)
        self.mapping: aes = mapping if mapping is not None else aes()

        # Future components (facets/scales/theme/guides/coords) will live here.
        self.layers: Layers = Layers()
        self.labels: dict[str, str] = {}
        self.theme: dict[str, Any] = {}

    def __iadd__(self, other: PlotAddable | list[PlotAddable] | None):
        if other is None:
            return self
        if isinstance(other, list):
            for item in other:
                item.__radd__(self)
            return self
        other.__radd__(self)
        return self

    def __add__(self, rhs: PlotAddable | list[PlotAddable] | None) -> "ggplot":
        p = deepcopy(self)
        return p.__iadd__(rhs)

    def __radd__(self, other: Any) -> "ggplot":
        raise PlotAddError(f"Cannot add ggplot to {type(other)!r}")
