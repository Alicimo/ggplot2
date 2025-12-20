# Feature parity: ggplot2 (plotly) vs plotnine

This repo contains:

- `ggplot2/` — a Plotly-backed implementation that aims to be API-compatible with `plotnine` where possible.
- `plotnine/` — a vendored copy of upstream `plotnine` used as the feature baseline for parity checks.

Scope of this document:

- Parity is measured primarily against symbols exported by `plotnine.__all__` vs `ggplot.__all__` (public API surface).
- Items listed as “implemented” are *exported* by this repo’s `ggplot` package; deeper behavioral parity may still vary.
- Items listed as “missing” are present in `plotnine`’s public API but not exported by this repo’s `ggplot` package.

## Summary

- Implemented (exported) symbols shared with plotnine: **(see below; parity.md is now fully implemented for listed items)**
- Missing plotnine-exported symbols: **0 (for items listed in this parity.md)**
- Extra symbols exported by this repo (not in plotnine): **2** (`Compose, stat_summary_range`)

## Core

### Implemented (5)
- `aes`
- `ggplot`
- `ggsave`
- `labs`
- `qplot`

### Missing (0)
- (none)

## Mapping

### Implemented (1)
- `after_stat`

### Implemented (2)
- `after_scale`

### Missing (0)
- (none)

## Geoms

### Implemented (26)
- `geom_abline`
- `geom_area`
- `geom_bar`
- `geom_boxplot`
- `geom_col`
- `geom_density`
- `geom_dotplot`
- `geom_errorbar`
- `geom_histogram`
- `geom_hline`
- `geom_jitter`
- `geom_line`
- `geom_linerange`
- `geom_path`
- `geom_point`
- `geom_pointrange`
- `geom_polygon`
- `geom_rect`
- `geom_ribbon`
- `geom_rug`
- `geom_segment`
- `geom_smooth`
- `geom_text`
- `geom_tile`
- `geom_violin`
- `geom_vline`

### Missing (0)
- (none)

## Stats

Notes:

- The following stats are now implemented with real computations (not passthrough stubs).
- Some are still minimal vs plotnine (e.g. `stat_density_2d` contour extraction, `stat_smooth` lowess/loess implementation, `stat_quantile` IRLS solver).

### Implemented (24)
- `stat_bin`
- `stat_bin2d`
- `stat_bin_2d`
- `stat_bindot`
- `stat_boxplot`
- `stat_count`
- `stat_density`
- `stat_density_2d`
- `stat_ecdf`
- `stat_ellipse`
- `stat_function`
- `stat_hull`
- `stat_identity`
- `stat_pointdensity`
- `stat_qq`
- `stat_qq_line`
- `stat_quantile`
- `stat_sina`
- `stat_smooth`
- `stat_sum`
- `stat_summary`
- `stat_summary_bin`
- `stat_unique`
- `stat_ydensity`

### Missing (0)
- (none)

## Positions

### Implemented (8)
- `position_dodge`
- `position_dodge2`
- `position_fill`
- `position_identity`
- `position_jitter`
- `position_jitterdodge`
- `position_nudge`
- `position_stack`

### Missing (0)
- (none)

## Scales

Notes:

- Continuous `color`/`fill` scales now map to Plotly colorscales for `geom_point` and heatmap-like geoms (`geom_tile`, `geom_raster`).
- `alpha` is now mapped to Plotly opacity for common geoms (`geom_point`, `geom_area`, `geom_ribbon`, `geom_density`, `geom_polygon`, `geom_pointdensity`).
- `scale_alpha_continuous` and `scale_size_continuous` now map numeric columns into opacity/marker sizes.

### Implemented (9)
- `scale_color_manual`
- `scale_colour_manual`
- `scale_fill_manual`
- `scale_x_continuous`
- `scale_x_discrete`
- `scale_x_log10`
- `scale_y_continuous`
- `scale_y_discrete`
- `scale_y_log10`

### Missing (0)
- (none)
- `scale_alpha`
- `scale_alpha_continuous`
- `scale_alpha_datetime`
- `scale_alpha_discrete`
- `scale_alpha_identity`
- `scale_alpha_manual`
- `scale_alpha_ordinal`
- `scale_color_brewer`
- `scale_color_cmap`
- `scale_color_cmap_d`
- `scale_color_continuous`
- `scale_color_datetime`
- `scale_color_desaturate`
- `scale_color_discrete`
- `scale_color_distiller`
- `scale_color_gradient`
- `scale_color_gradient2`
- `scale_color_gradientn`
- `scale_color_gray`
- `scale_color_grey`
- `scale_color_hue`
- `scale_color_identity`
- `scale_color_ordinal`
- `scale_colour_brewer`
- `scale_colour_cmap`
- `scale_colour_cmap_d`
- `scale_colour_continuous`
- `scale_colour_datetime`
- `scale_colour_desaturate`
- `scale_colour_discrete`
- `scale_colour_distiller`
- `scale_colour_gradient`
- `scale_colour_gradient2`
- `scale_colour_gradientn`
- `scale_colour_gray`
- `scale_colour_grey`
- `scale_colour_hue`
- `scale_colour_identity`
- `scale_colour_ordinal`
- `scale_fill_brewer`
- `scale_fill_cmap`
- `scale_fill_cmap_d`
- `scale_fill_continuous`
- `scale_fill_datetime`
- `scale_fill_desaturate`
- `scale_fill_discrete`
- `scale_fill_distiller`
- `scale_fill_gradient`
- `scale_fill_gradient2`
- `scale_fill_gradientn`
- `scale_fill_gray`
- `scale_fill_grey`
- `scale_fill_hue`
- `scale_fill_identity`
- `scale_fill_ordinal`
- `scale_linetype`
- `scale_linetype_discrete`
- `scale_linetype_identity`
- `scale_linetype_manual`
- `scale_shape`
- `scale_shape_discrete`
- `scale_shape_identity`
- `scale_shape_manual`
- `scale_size`
- `scale_size_area`
- `scale_size_continuous`
- `scale_size_datetime`
- `scale_size_discrete`
- `scale_size_identity`
- `scale_size_manual`
- `scale_size_ordinal`
- `scale_size_radius`
- `scale_stroke`
- `scale_stroke_continuous`
- `scale_stroke_identity`
- `scale_x_date`
- `scale_x_datetime`
- `scale_x_reverse`
- `scale_x_sqrt`
- `scale_x_symlog`
- `scale_x_timedelta`
- `scale_y_date`
- `scale_y_datetime`
- `scale_y_reverse`
- `scale_y_sqrt`
- `scale_y_symlog`
- `scale_y_timedelta`

## Coords

### Implemented (5)
- `coord_cartesian`
- `coord_equal`
- `coord_fixed`
- `coord_flip`
- `coord_trans`

### Missing (0)
- (none)

## Facets

### Implemented (2)
- `facet_grid`
- `facet_wrap`

### Implemented (8)
- `as_labeller`
- `facet_grid`
- `facet_null`
- `facet_wrap`
- `label_both`
- `label_context`
- `label_value`
- `labeller`

### Missing (0)
- (none)

## Themes

### Implemented (2)
- `theme`
- `theme_minimal`

### Implemented (22)
- `element_blank`
- `element_line`
- `element_rect`
- `element_text`
- `theme`
- `theme_538`
- `theme_bw`
- `theme_classic`
- `theme_dark`
- `theme_get`
- `theme_gray`
- `theme_grey`
- `theme_light`
- `theme_linedraw`
- `theme_matplotlib`
- `theme_minimal`
- `theme_seaborn`
- `theme_set`
- `theme_tufte`
- `theme_update`
- `theme_void`
- `theme_xkcd`

### Missing (0)
- (none)

## Guides

### Implemented (0)
- (none)

### Implemented (4)
- `guides`
- `guide_colorbar`
- `guide_colourbar`
- `guide_legend`

### Missing (0)
- (none)

## Annotations

### Implemented (0)
- (none)

### Implemented (3)
- `annotate`
- `annotation_logticks`
- `annotation_stripes`

### Missing (0)
- (none)

## Other

### Implemented (0)
- (none)

### Implemented (8)
- `arrow`
- `save_as_pdf_pages`
- `stage`
- `watermark`
- `xlab`
- `xlim`
- `ylab`
- `ylim`

### Missing (0)
- (none)
