from __future__ import annotations

from dataclasses import dataclass

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
