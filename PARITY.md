# Parity tracker

This document tracks feature parity between this project (`ggplot2` distribution / `ggplot` namespace) and upstream `plotnine`.

## Principles

- Prefer expanding compatibility via `tests/compat/` (renderer-agnostic tests) rather than importing matplotlib/mizani.
- Keep `tests/plotnine_upstream/` vendored for reference, but do not expect it to pass without significant adaptation.
- Each feature should land with at least one compat test.

## Status (high level)

### Core objects

- [x] `ggplot` + additive API (`+`)
- [x] `aes` + simple expression evaluation
- [x] `after_stat` (basic)
- [x] `ggsave` (Plotly + Kaleido)
- [ ] `qplot`
- [ ] plot composition operators (`|`, `/`, etc.)

### Geoms

Implemented:

- [x] `geom_point`
- [x] `geom_line`
- [x] `geom_path`
- [x] `geom_bar`
- [x] `geom_histogram`
- [x] `geom_segment`
- [x] `geom_text`
- [x] `geom_rect`
- [x] `geom_ribbon`
- [x] `geom_area`
- [x] `geom_vline`

Missing (examples of big ones):

- [ ] `geom_boxplot`, `geom_violin`
- [ ] `geom_smooth`
- [ ] `geom_tile`, `geom_polygon`
- [ ] error bars / ranges (`geom_errorbar`, `geom_linerange`, ...)

### Stats

- [x] `stat_identity`
- [x] `stat_count`
- [x] `stat_bin` (minimal)
- [ ] `stat_smooth`, `stat_density`, `stat_boxplot`, ...

### Positions

- [x] identity
- [x] stack (minimal)
- [x] dodge (minimal)
- [ ] jitter, jitterdodge, nudge, dodge2, ...

### Scales

- [x] `scale_x_continuous`, `scale_y_continuous` (limits + breaks)
- [x] `scale_color_manual`, `scale_fill_manual`
- [ ] discrete position scales (`scale_x_discrete`, `scale_y_discrete`)
- [ ] log/date transforms
- [ ] color scales beyond manual

### Facets

- [x] `facet_wrap` (single variable)
- [ ] `facet_grid`
- [ ] labellers

### Coords

- [x] cartesian (implicit)
- [ ] `coord_flip`, `coord_fixed`, `coord_trans`, `coord_polar`

