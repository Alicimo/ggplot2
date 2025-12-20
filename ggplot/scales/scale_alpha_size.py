from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .scale_continuous import scale_continuous


@dataclass
class ScaleAlphaContinuous(scale_continuous):
    range: tuple[float, float] = (0.1, 1.0)

    def map(self, values, *, domain: tuple[float, float]):
        t = self.norm(values, domain=domain)
        lo, hi = float(self.range[0]), float(self.range[1])
        return lo + t * (hi - lo)


def scale_alpha_continuous(*, limits=None, range: tuple[float, float] = (0.1, 1.0)):
    return ScaleAlphaContinuous(aesthetic="alpha", limits=limits, range=range)


@dataclass
class ScaleSizeContinuous(scale_continuous):
    range: tuple[float, float] = (2.0, 10.0)

    def map(self, values, *, domain: tuple[float, float]):
        t = self.norm(values, domain=domain)
        lo, hi = float(self.range[0]), float(self.range[1])
        return lo + t * (hi - lo)


def scale_size_continuous(*, limits=None, range: tuple[float, float] = (2.0, 10.0)):
    return ScaleSizeContinuous(aesthetic="size", limits=limits, range=range)


@dataclass
class ScaleSizeArea(scale_continuous):
    max_size: float = 10.0

    def map(self, values, *, domain: tuple[float, float]):
        # Map to area, then take sqrt to get radius-like marker size.
        t = self.norm(values, domain=domain)
        area = t * float(self.max_size) ** 2
        return np.sqrt(area)


def scale_size_area(*, limits=None, max_size: float = 10.0):
    return ScaleSizeArea(aesthetic="size", limits=limits, max_size=max_size)


@dataclass
class ScaleSizeRadius(scale_continuous):
    range: tuple[float, float] = (1.0, 6.0)

    def map(self, values, *, domain: tuple[float, float]):
        t = self.norm(values, domain=domain)
        lo, hi = float(self.range[0]), float(self.range[1])
        return lo + t * (hi - lo)


def scale_size_radius(*, limits=None, range: tuple[float, float] = (1.0, 6.0)):
    return ScaleSizeRadius(aesthetic="size", limits=limits, range=range)


@dataclass
class ScaleStrokeContinuous(scale_continuous):
    range: tuple[float, float] = (0.5, 3.0)

    def map(self, values, *, domain: tuple[float, float]):
        t = self.norm(values, domain=domain)
        lo, hi = float(self.range[0]), float(self.range[1])
        return lo + t * (hi - lo)


def scale_stroke_continuous(*, limits=None, range: tuple[float, float] = (0.5, 3.0)):
    return ScaleStrokeContinuous(aesthetic="stroke", limits=limits, range=range)
