from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from .scale_discrete import (
    scale_color_manual,
    scale_discrete,
    scale_fill_manual,
)


@dataclass
class scale_identity(scale_discrete):
    def map(self, series):
        return series


def scale_alpha(*args: Any, **kwargs: Any):
    return scale_discrete(aesthetic="alpha")


def scale_alpha_continuous(*args: Any, **kwargs: Any):
    return scale_alpha()


def scale_alpha_datetime(*args: Any, **kwargs: Any):
    return scale_alpha()


def scale_alpha_discrete(*args: Any, **kwargs: Any):
    return scale_alpha()


def scale_alpha_identity(*args: Any, **kwargs: Any):
    return scale_identity(aesthetic="alpha")


def scale_alpha_manual(values: Mapping[Any, Any]):
    return scale_discrete(aesthetic="alpha", values=values)


def scale_alpha_ordinal(*args: Any, **kwargs: Any):
    return scale_alpha_discrete()


def scale_color_identity():
    return scale_identity(aesthetic="color")


def scale_colour_identity():
    return scale_color_identity()


def scale_fill_identity():
    return scale_identity(aesthetic="fill")


def scale_color_discrete(*args: Any, **kwargs: Any):
    return scale_color_manual(values={})


def scale_colour_discrete(*args: Any, **kwargs: Any):
    return scale_color_discrete()


def scale_fill_discrete(*args: Any, **kwargs: Any):
    return scale_fill_manual(values={})


def scale_shape(*args: Any, **kwargs: Any):
    return scale_discrete(aesthetic="shape")


def scale_shape_discrete(*args: Any, **kwargs: Any):
    return scale_shape()


def scale_shape_identity(*args: Any, **kwargs: Any):
    return scale_identity(aesthetic="shape")


def scale_shape_manual(values: Mapping[Any, Any]):
    return scale_discrete(aesthetic="shape", values=values)


def scale_size(*args: Any, **kwargs: Any):
    return scale_discrete(aesthetic="size")


def scale_size_area(*args: Any, **kwargs: Any):
    return scale_size()


def scale_size_continuous(*args: Any, **kwargs: Any):
    return scale_size()


def scale_size_datetime(*args: Any, **kwargs: Any):
    return scale_size()


def scale_size_discrete(*args: Any, **kwargs: Any):
    return scale_size()


def scale_size_identity(*args: Any, **kwargs: Any):
    return scale_identity(aesthetic="size")


def scale_size_manual(values: Mapping[Any, Any]):
    return scale_discrete(aesthetic="size", values=values)


def scale_size_ordinal(*args: Any, **kwargs: Any):
    return scale_size_discrete()


def scale_size_radius(*args: Any, **kwargs: Any):
    return scale_size()


def scale_stroke(*args: Any, **kwargs: Any):
    return scale_discrete(aesthetic="stroke")


def scale_stroke_continuous(*args: Any, **kwargs: Any):
    return scale_stroke()


def scale_stroke_identity(*args: Any, **kwargs: Any):
    return scale_identity(aesthetic="stroke")


def scale_linetype(*args: Any, **kwargs: Any):
    return scale_discrete(aesthetic="linetype")


def scale_linetype_discrete(*args: Any, **kwargs: Any):
    return scale_linetype()


def scale_linetype_identity(*args: Any, **kwargs: Any):
    return scale_identity(aesthetic="linetype")


def scale_linetype_manual(values: Mapping[Any, Any]):
    return scale_discrete(aesthetic="linetype", values=values)


# Many named color scales are currently aliases to manual/discrete.


def _alias_color_scale(*args: Any, **kwargs: Any):
    return scale_color_discrete()


scale_color_brewer = _alias_color_scale
scale_color_cmap = _alias_color_scale
scale_color_cmap_d = _alias_color_scale
scale_color_continuous = _alias_color_scale
scale_color_datetime = _alias_color_scale
scale_color_desaturate = _alias_color_scale
scale_color_distiller = _alias_color_scale
scale_color_gradient = _alias_color_scale
scale_color_gradient2 = _alias_color_scale
scale_color_gradientn = _alias_color_scale
scale_color_gray = _alias_color_scale
scale_color_grey = _alias_color_scale
scale_color_hue = _alias_color_scale
scale_color_ordinal = _alias_color_scale

scale_colour_brewer = _alias_color_scale
scale_colour_cmap = _alias_color_scale
scale_colour_cmap_d = _alias_color_scale
scale_colour_continuous = _alias_color_scale
scale_colour_datetime = _alias_color_scale
scale_colour_desaturate = _alias_color_scale
scale_colour_distiller = _alias_color_scale
scale_colour_gradient = _alias_color_scale
scale_colour_gradient2 = _alias_color_scale
scale_colour_gradientn = _alias_color_scale
scale_colour_gray = _alias_color_scale
scale_colour_grey = _alias_color_scale
scale_colour_hue = _alias_color_scale
scale_colour_ordinal = _alias_color_scale


def _alias_fill_scale(*args: Any, **kwargs: Any):
    return scale_fill_discrete()


scale_fill_brewer = _alias_fill_scale
scale_fill_cmap = _alias_fill_scale
scale_fill_cmap_d = _alias_fill_scale
scale_fill_continuous = _alias_fill_scale
scale_fill_datetime = _alias_fill_scale
scale_fill_desaturate = _alias_fill_scale
scale_fill_distiller = _alias_fill_scale
scale_fill_gradient = _alias_fill_scale
scale_fill_gradient2 = _alias_fill_scale
scale_fill_gradientn = _alias_fill_scale
scale_fill_gray = _alias_fill_scale
scale_fill_grey = _alias_fill_scale
scale_fill_hue = _alias_fill_scale
scale_fill_ordinal = _alias_fill_scale
