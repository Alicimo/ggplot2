"""ggplot2 (distribution) / ggplot (import namespace).

This package is intentionally minimal in Phase 0: core objects and the additive
API wiring. Rendering/geoms/stats/scales come in later phases.
"""

from .ggplot import ggplot
from .mapping.aes import aes
from .addables import labs, theme

__all__ = ["ggplot", "aes", "labs", "theme"]
