"""ggplot2 (distribution) / ggplot (import namespace).

This package is intentionally minimal in Phase 0: core objects and the additive
API wiring. Rendering/geoms/stats/scales come in later phases.
"""

from .ggplot import ggplot
from .geoms.geom_point import geom_point
from .ggsave import ggsave
from .mapping.aes import aes
from .mapping.evaluation import after_stat
from .addables import labs, theme
from .scales.scale_xy import scale_x_continuous, scale_y_continuous
from .facets.facet_wrap import facet_wrap

__all__ = [
    "ggplot",
    "aes",
    "after_stat",
    "labs",
    "theme",
    "geom_point",
    "ggsave",
    "scale_x_continuous",
    "scale_y_continuous",
    "facet_wrap",
]
