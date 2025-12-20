"""ggplot2 (distribution) / ggplot (import namespace).

This package is intentionally minimal in Phase 0: core objects and the additive
API wiring. Rendering/geoms/stats/scales come in later phases.
"""

from .addables import labs
from .annotations import annotate, annotation_logticks, annotation_stripes
from .composition import Compose
from .coords.coord_cartesian import coord_cartesian
from .coords.coord_equal import coord_equal
from .coords.coord_fixed import coord_fixed
from .coords.coord_flip import coord_flip
from .coords.coord_trans import coord_trans
from .facets.facet_grid import facet_grid
from .facets.facet_wrap import facet_wrap
from .facets.labelling import (
    as_labeller,
    facet_null,
    label_both,
    label_context,
    label_value,
    labeller,
)
from .geoms.geom_abline import geom_abline
from .geoms.geom_area import geom_area
from .geoms.geom_bar import geom_bar
from .geoms.geom_bin_2d import geom_bin2d, geom_bin_2d
from .geoms.geom_blank import geom_blank
from .geoms.geom_boxplot import geom_boxplot
from .geoms.geom_col import geom_col
from .geoms.geom_count import geom_count
from .geoms.geom_crossbar import geom_crossbar
from .geoms.geom_density import geom_density
from .geoms.geom_density_2d import geom_density_2d
from .geoms.geom_dotplot import geom_dotplot
from .geoms.geom_errorbar import geom_errorbar
from .geoms.geom_errorbarh import geom_errorbarh
from .geoms.geom_freqpoly import geom_freqpoly
from .geoms.geom_histogram import geom_histogram
from .geoms.geom_hline import geom_hline
from .geoms.geom_jitter import geom_jitter
from .geoms.geom_label import geom_label
from .geoms.geom_line import geom_line
from .geoms.geom_linerange import geom_linerange
from .geoms.geom_map import geom_map
from .geoms.geom_path import geom_path
from .geoms.geom_point import geom_point
from .geoms.geom_pointdensity import geom_pointdensity
from .geoms.geom_pointrange import geom_pointrange
from .geoms.geom_polygon import geom_polygon
from .geoms.geom_qq import geom_qq
from .geoms.geom_qq_line import geom_qq_line
from .geoms.geom_quantile import geom_quantile
from .geoms.geom_raster import geom_raster
from .geoms.geom_rect import geom_rect
from .geoms.geom_ribbon import geom_ribbon
from .geoms.geom_rug import geom_rug
from .geoms.geom_segment import geom_segment
from .geoms.geom_sina import geom_sina
from .geoms.geom_smooth import geom_smooth
from .geoms.geom_spoke import geom_spoke
from .geoms.geom_step import geom_step
from .geoms.geom_text import geom_text
from .geoms.geom_tile import geom_tile
from .geoms.geom_violin import geom_violin
from .geoms.geom_vline import geom_vline
from .ggplot import ggplot
from .ggsave import ggsave
from .guides import guide_colorbar, guide_colourbar, guide_legend, guides
from .limits import expand_limits, lims, xlim, ylim
from .mapping.aes import aes
from .mapping.evaluation import after_scale, after_stat
from .other import arrow, stage, watermark
from .positions.position_dodge import position_dodge
from .positions.position_dodge2 import position_dodge2
from .positions.position_fill import position_fill
from .positions.position_identity import position_identity
from .positions.position_jitter import position_jitter
from .positions.position_jitterdodge import position_jitterdodge
from .positions.position_nudge import position_nudge
from .positions.position_stack import position_stack
from .qplot import qplot
from .save_as_pdf_pages import save_as_pdf_pages
from .scales.compat import (
    scale_alpha,
    scale_alpha_continuous,
    scale_alpha_datetime,
    scale_alpha_discrete,
    scale_alpha_identity,
    scale_alpha_manual,
    scale_alpha_ordinal,
    scale_color_brewer,
    scale_color_cmap,
    scale_color_cmap_d,
    scale_color_continuous,
    scale_color_datetime,
    scale_color_desaturate,
    scale_color_discrete,
    scale_color_distiller,
    scale_color_gradient,
    scale_color_gradient2,
    scale_color_gradientn,
    scale_color_gray,
    scale_color_grey,
    scale_color_hue,
    scale_color_identity,
    scale_color_ordinal,
    scale_colour_brewer,
    scale_colour_cmap,
    scale_colour_cmap_d,
    scale_colour_continuous,
    scale_colour_datetime,
    scale_colour_desaturate,
    scale_colour_discrete,
    scale_colour_distiller,
    scale_colour_gradient,
    scale_colour_gradient2,
    scale_colour_gradientn,
    scale_colour_gray,
    scale_colour_grey,
    scale_colour_hue,
    scale_colour_identity,
    scale_colour_ordinal,
    scale_fill_brewer,
    scale_fill_cmap,
    scale_fill_cmap_d,
    scale_fill_continuous,
    scale_fill_datetime,
    scale_fill_desaturate,
    scale_fill_discrete,
    scale_fill_distiller,
    scale_fill_gradient,
    scale_fill_gradient2,
    scale_fill_gradientn,
    scale_fill_gray,
    scale_fill_grey,
    scale_fill_hue,
    scale_fill_identity,
    scale_fill_ordinal,
    scale_linetype,
    scale_linetype_discrete,
    scale_linetype_identity,
    scale_linetype_manual,
    scale_shape,
    scale_shape_discrete,
    scale_shape_identity,
    scale_shape_manual,
    scale_size,
    scale_size_area,
    scale_size_continuous,
    scale_size_datetime,
    scale_size_discrete,
    scale_size_identity,
    scale_size_manual,
    scale_size_ordinal,
    scale_size_radius,
    scale_stroke,
    scale_stroke_continuous,
    scale_stroke_identity,
)
from .scales.scale_discrete import (
    scale_color_manual,
    scale_colour_manual,
    scale_fill_manual,
)
from .scales.scale_transforms import (
    scale_x_date,
    scale_x_datetime,
    scale_x_log10,
    scale_x_reverse,
    scale_x_sqrt,
    scale_x_symlog,
    scale_x_timedelta,
    scale_y_date,
    scale_y_datetime,
    scale_y_log10,
    scale_y_reverse,
    scale_y_sqrt,
    scale_y_symlog,
    scale_y_timedelta,
)
from .scales.scale_xy import scale_x_continuous, scale_y_continuous
from .scales.scale_xy_discrete import scale_x_discrete, scale_y_discrete
from .stats.addables import (
    stat_bin,
    stat_boxplot,
    stat_count,
    stat_density,
    stat_identity,
    stat_quantile,
    stat_smooth,
    stat_summary,
    stat_summary_range,
)
from .stats.compat import (
    stat_bin2d,
    stat_bin_2d,
    stat_bindot,
    stat_density_2d,
    stat_ecdf,
    stat_ellipse,
    stat_function,
    stat_hull,
    stat_pointdensity,
    stat_qq,
    stat_qq_line,
    stat_sina,
    stat_sum,
    stat_summary_bin,
    stat_unique,
    stat_ydensity,
)
from .themes.elements import element_blank, element_line, element_rect, element_text
from .themes.theme import theme
from .themes.theme_defaults import (
    theme_538,
    theme_bw,
    theme_classic,
    theme_dark,
    theme_gray,
    theme_grey,
    theme_light,
    theme_linedraw,
    theme_matplotlib,
    theme_minimal,
    theme_seaborn,
    theme_tufte,
    theme_void,
    theme_xkcd,
)
from .themes.theme_registry import theme_get, theme_set, theme_update
from .title import ggtitle, xlab, ylab

__all__ = [
    "ggplot",
    "aes",
    "after_stat",
    "after_scale",
    "stat_summary",
    "stat_summary_range",
    "stat_identity",
    "stat_count",
    "stat_bin",
    "stat_bin2d",
    "stat_bin_2d",
    "stat_bindot",
    "stat_boxplot",
    "stat_density",
    "stat_density_2d",
    "stat_ecdf",
    "stat_ellipse",
    "stat_function",
    "stat_hull",
    "stat_pointdensity",
    "stat_qq",
    "stat_qq_line",
    "stat_quantile",
    "stat_sina",
    "stat_smooth",
    "stat_sum",
    "stat_summary_bin",
    "stat_unique",
    "stat_ydensity",
    "labs",
    "theme",
    "theme_minimal",
    "element_blank",
    "element_line",
    "element_rect",
    "element_text",
    "theme_get",
    "theme_set",
    "theme_update",
    "theme_538",
    "theme_bw",
    "theme_classic",
    "theme_dark",
    "theme_gray",
    "theme_grey",
    "theme_light",
    "theme_linedraw",
    "theme_matplotlib",
    "theme_seaborn",
    "theme_tufte",
    "theme_void",
    "theme_xkcd",
    "position_stack",
    "position_dodge",
    "position_dodge2",
    "position_identity",
    "position_jitter",
    "position_nudge",
    "position_jitterdodge",
    "position_fill",
    "coord_cartesian",
    "coord_equal",
    "coord_flip",
    "coord_fixed",
    "coord_trans",
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
    "geom_density",
    "geom_rug",
    "geom_dotplot",
    "geom_jitter",
    "geom_blank",
    "geom_bin2d",
    "geom_bin_2d",
    "geom_count",
    "geom_crossbar",
    "geom_density_2d",
    "geom_errorbarh",
    "geom_freqpoly",
    "geom_label",
    "geom_map",
    "geom_pointdensity",
    "geom_qq",
    "geom_qq_line",
    "geom_quantile",
    "geom_raster",
    "geom_sina",
    "geom_spoke",
    "geom_step",
    "ggsave",
    "qplot",
    "save_as_pdf_pages",
    "Compose",
    "expand_limits",
    "lims",
    "xlim",
    "ylim",
    "ggtitle",
    "xlab",
    "ylab",
    "guides",
    "guide_legend",
    "guide_colorbar",
    "guide_colourbar",
    "annotate",
    "annotation_logticks",
    "annotation_stripes",
    "arrow",
    "stage",
    "watermark",
    "scale_x_continuous",
    "scale_y_continuous",
    "scale_x_discrete",
    "scale_y_discrete",
    "scale_color_manual",
    "scale_colour_manual",
    "scale_fill_manual",
    "scale_x_log10",
    "scale_y_log10",
    "scale_x_date",
    "scale_y_date",
    "scale_x_datetime",
    "scale_y_datetime",
    "scale_x_timedelta",
    "scale_y_timedelta",
    "scale_x_reverse",
    "scale_y_reverse",
    "scale_x_sqrt",
    "scale_y_sqrt",
    "scale_x_symlog",
    "scale_y_symlog",
    "scale_alpha",
    "scale_alpha_continuous",
    "scale_alpha_datetime",
    "scale_alpha_discrete",
    "scale_alpha_identity",
    "scale_alpha_manual",
    "scale_alpha_ordinal",
    "scale_color_brewer",
    "scale_color_cmap",
    "scale_color_cmap_d",
    "scale_color_continuous",
    "scale_color_datetime",
    "scale_color_desaturate",
    "scale_color_discrete",
    "scale_color_distiller",
    "scale_color_gradient",
    "scale_color_gradient2",
    "scale_color_gradientn",
    "scale_color_gray",
    "scale_color_grey",
    "scale_color_hue",
    "scale_color_identity",
    "scale_color_ordinal",
    "scale_colour_brewer",
    "scale_colour_cmap",
    "scale_colour_cmap_d",
    "scale_colour_continuous",
    "scale_colour_datetime",
    "scale_colour_desaturate",
    "scale_colour_discrete",
    "scale_colour_distiller",
    "scale_colour_gradient",
    "scale_colour_gradient2",
    "scale_colour_gradientn",
    "scale_colour_gray",
    "scale_colour_grey",
    "scale_colour_hue",
    "scale_colour_identity",
    "scale_colour_ordinal",
    "scale_fill_brewer",
    "scale_fill_cmap",
    "scale_fill_cmap_d",
    "scale_fill_continuous",
    "scale_fill_datetime",
    "scale_fill_desaturate",
    "scale_fill_discrete",
    "scale_fill_distiller",
    "scale_fill_gradient",
    "scale_fill_gradient2",
    "scale_fill_gradientn",
    "scale_fill_gray",
    "scale_fill_grey",
    "scale_fill_hue",
    "scale_fill_identity",
    "scale_fill_ordinal",
    "scale_linetype",
    "scale_linetype_discrete",
    "scale_linetype_identity",
    "scale_linetype_manual",
    "scale_shape",
    "scale_shape_discrete",
    "scale_shape_identity",
    "scale_shape_manual",
    "scale_size",
    "scale_size_area",
    "scale_size_continuous",
    "scale_size_datetime",
    "scale_size_discrete",
    "scale_size_identity",
    "scale_size_manual",
    "scale_size_ordinal",
    "scale_size_radius",
    "scale_stroke",
    "scale_stroke_continuous",
    "scale_stroke_identity",
    "facet_wrap",
    "facet_grid",
    "as_labeller",
    "facet_null",
    "label_both",
    "label_context",
    "label_value",
    "labeller",
]
