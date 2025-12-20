from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class element_blank:
    pass


@dataclass(frozen=True)
class element_line:
    color: Any | None = None
    size: float | None = None


@dataclass(frozen=True)
class element_rect:
    fill: Any | None = None
    color: Any | None = None


@dataclass(frozen=True)
class element_text:
    color: Any | None = None
    size: float | None = None
