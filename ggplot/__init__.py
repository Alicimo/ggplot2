"""ggplot2 (distribution) / ggplot (import namespace).

This package is intentionally minimal in Phase 0: core objects and the additive
API wiring. Rendering/geoms/stats/scales come in later phases.
"""

from .ggplot import ggplot
from .geoms.geom_point import geom_point
from .geoms.geom_line import geom_line
from .geoms.geom_bar import geom_bar
from .geoms.geom_col import geom_col
from .geoms.geom_histogram import geom_histogram
from .geoms.geom_path import geom_path
from .geoms.geom_segment import geom_segment
from .geoms.geom_text import geom_text
from .geoms.geom_rect import geom_rect
from .geoms.geom_ribbon import geom_ribbon
from .geoms.geom_area import geom_area
from .geoms.geom_vline import geom_vline
from .geoms.geom_boxplot import geom_boxplot
from .geoms.geom_violin import geom_violin
from .geoms.geom_smooth import geom_smooth
from .geoms.geom_tile import geom_tile
from .geoms.geom_polygon import geom_polygon
from .geoms.geom_hline import geom_hline
from .geoms.geom_abline import geom_abline
from .geoms.geom_linerange import geom_linerange
from .geoms.geom_errorbar import geom_errorbar
from .geoms.geom_pointrange import geom_pointrange
from .ggsave import ggsave
from .mapping.aes import aes
from .mapping.evaluation import after_stat
from .stats.addables import stat_summary, stat_summary_range
from .addables import labs
from .scales.scale_xy import scale_x_continuous, scale_y_continuous
from .scales.scale_xy_discrete import scale_x_discrete, scale_y_discrete
from .scales.scale_discrete import (
    scale_color_manual,
    scale_colour_manual,
    scale_fill_manual,
)
from .facets.facet_wrap import facet_wrap
from .facets.facet_grid import facet_grid
from .themes.theme import theme
from .themes.theme_defaults import theme_minimal
from .positions.position_stack import position_stack
from .positions.position_dodge import position_dodge
from .positions.position_jitter import position_jitter
from .positions.position_nudge import position_nudge
from .coords.coord_cartesian import coord_cartesian
from .coords.coord_flip import coord_flip

__all__ = [
    "ggplot",
    "aes",
    "after_stat",
    "stat_summary",
    "stat_summary_range",
    "labs",
    "theme",
    "theme_minimal",
    "position_stack",
    "position_dodge",
    "position_jitter",
    "position_nudge",
    "coord_cartesian",
    "coord_flip",
    "geom_point",
    "geom_line",
    "geom_bar",
    "geom_col",
    "geom_histogram",
    "geom_path",
    "geom_segment",
    "geom_text",
    "geom_rect",
    "geom_ribbon",
    "geom_area",
    "geom_vline",
    "geom_boxplot",
    "geom_violin",
    "geom_smooth",
    "geom_tile",
    "geom_polygon",
    "geom_hline",
    "geom_abline",
    "geom_linerange",
    "geom_errorbar",
    "geom_pointrange",
    "ggsave",
    "scale_x_continuous",
    "scale_y_continuous",
    "scale_x_discrete",
    "scale_y_discrete",
    "scale_color_manual",
    "scale_colour_manual",
    "scale_fill_manual",
    "facet_wrap",
    "facet_grid",
]
