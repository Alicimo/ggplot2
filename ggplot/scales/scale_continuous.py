from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from .scale import scale


def _as_float_array(values) -> np.ndarray:
    arr = np.asarray(values, dtype=float)
    return arr


@dataclass
class scale_continuous(scale):
    limits: tuple[float, float] | None = None
    palette: str | list[list[Any]] | None = None
    oob: str = "squish"
    guide: str = "colorbar"

    def train(self, values) -> tuple[float, float]:
        if self.limits is not None:
            return (float(self.limits[0]), float(self.limits[1]))
        arr = _as_float_array(values)
        arr = arr[np.isfinite(arr)]
        if arr.size == 0:
            return (0.0, 1.0)
        return (float(arr.min()), float(arr.max()))

    def norm(self, values, *, domain: tuple[float, float]) -> np.ndarray:
        lo, hi = domain
        arr = _as_float_array(values)
        if hi == lo:
            return np.zeros_like(arr)
        t = (arr - lo) / (hi - lo)
        if self.oob == "squish":
            t = np.clip(t, 0.0, 1.0)
        return t


def scale_color_continuous(
    *, limits=None, palette: str | None = "Viridis"
) -> scale_continuous:
    return scale_continuous(aesthetic="color", limits=limits, palette=palette)


def scale_colour_continuous(
    *, limits=None, palette: str | None = "Viridis"
) -> scale_continuous:
    return scale_color_continuous(limits=limits, palette=palette)


def scale_fill_continuous(
    *, limits=None, palette: str | None = "Viridis"
) -> scale_continuous:
    return scale_continuous(aesthetic="fill", limits=limits, palette=palette)


def scale_color_gradient(
    *, low: str = "#132B43", high: str = "#56B1F7", limits=None
) -> scale_continuous:
    return scale_continuous(
        aesthetic="color",
        limits=limits,
        palette=[[0.0, low], [1.0, high]],
    )


def scale_colour_gradient(
    *, low: str = "#132B43", high: str = "#56B1F7", limits=None
) -> scale_continuous:
    return scale_color_gradient(low=low, high=high, limits=limits)


def scale_fill_gradient(
    *, low: str = "#132B43", high: str = "#56B1F7", limits=None
) -> scale_continuous:
    return scale_continuous(
        aesthetic="fill",
        limits=limits,
        palette=[[0.0, low], [1.0, high]],
    )


def scale_color_gradient2(
    *,
    low: str = "#B2182B",
    mid: str = "#F7F7F7",
    high: str = "#2166AC",
    midpoint: float = 0.0,
    limits=None,
) -> scale_continuous:
    # Map midpoint to 0.5 by shifting limits around it if not explicitly provided.
    if limits is None:
        limits = (midpoint - 1.0, midpoint + 1.0)
    return scale_continuous(
        aesthetic="color",
        limits=limits,
        palette=[[0.0, low], [0.5, mid], [1.0, high]],
    )


def scale_colour_gradient2(**kwargs) -> scale_continuous:
    return scale_color_gradient2(**kwargs)


def scale_fill_gradient2(**kwargs) -> scale_continuous:
    out = scale_color_gradient2(**kwargs)
    out.aesthetic = "fill"
    return out


def scale_color_gradientn(*, colors: list[str], limits=None) -> scale_continuous:
    if not colors:
        raise ValueError("scale_color_gradientn requires colors")
    if len(colors) == 1:
        palette = [[0.0, colors[0]], [1.0, colors[0]]]
    else:
        stops = np.linspace(0.0, 1.0, len(colors))
        palette = [[float(s), c] for s, c in zip(stops, colors, strict=False)]
    return scale_continuous(aesthetic="color", limits=limits, palette=palette)


def scale_colour_gradientn(*, colors: list[str], limits=None) -> scale_continuous:
    return scale_color_gradientn(colors=colors, limits=limits)


def scale_fill_gradientn(*, colors: list[str], limits=None) -> scale_continuous:
    out = scale_color_gradientn(colors=colors, limits=limits)
    out.aesthetic = "fill"
    return out
