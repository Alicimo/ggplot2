from __future__ import annotations

from .stat_density import stat_density


def stat_ydensity(*, n: int = 256, bw=None):
    # In plotnine this is used for violins; our stat_density already computes
    # density over y.
    return stat_density(n=n, bw=bw)
