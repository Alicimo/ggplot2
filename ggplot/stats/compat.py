from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd

from .stat import stat


@dataclass
class passthrough_stat(stat):
    """Placeholder stat that returns the input unchanged."""

    def compute(self, df: pd.DataFrame, *, mapping: dict[str, Any]):
        return df


def stat_bin2d():
    return passthrough_stat()


def stat_bin_2d():
    return stat_bin2d()


def stat_bindot():
    return passthrough_stat()


def stat_density_2d():
    return passthrough_stat()


def stat_ecdf():
    return passthrough_stat()


def stat_ellipse():
    return passthrough_stat()


def stat_function():
    return passthrough_stat()


def stat_hull():
    return passthrough_stat()


def stat_pointdensity():
    return passthrough_stat()


def stat_qq():
    return passthrough_stat()


def stat_qq_line():
    return passthrough_stat()


def stat_sina():
    return passthrough_stat()


def stat_sum():
    return passthrough_stat()


def stat_summary_bin():
    return passthrough_stat()


def stat_unique():
    return passthrough_stat()


def stat_ydensity():
    return passthrough_stat()
