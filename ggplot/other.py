from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class arrow:
    # Stub container; used by some geoms for line end arrows in plotnine.
    length: float | None = None
    angle: float | None = None
    type: str | None = None
    ends: str | None = None


@dataclass(frozen=True)
class stage:
    # Stub for stage() used in scales.
    start: Any | None = None
    after_stat: Any | None = None
    after_scale: Any | None = None


@dataclass(frozen=True)
class watermark:
    # Stub; plotnine uses this for background image watermark.
    image: Any
