from __future__ import annotations

from typing import Any, Protocol, runtime_checkable

import pandas as pd

DataLike = pd.DataFrame | dict[str, Any] | list[dict[str, Any]] | None


class BuildResult(Protocol):
    """Internal build result protocol."""

    data: pd.DataFrame


@runtime_checkable
class PlotAddable(Protocol):
    def __radd__(self, other: "ggplot") -> "ggplot":  # noqa: F821
        ...

