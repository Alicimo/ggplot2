import math

import pandas as pd

from ggplot import (
    aes,
    geom_line,
    geom_point,
    ggplot,
    stat_bin2d,
    stat_ecdf,
    stat_hull,
    stat_qq,
    stat_qq_line,
    stat_quantile,
    stat_smooth,
    stat_sum,
)


def test_stat_ecdf_outputs_monotone_y():
    df = pd.DataFrame({"x": [3, 1, 2, 2]})
    out = stat_ecdf().compute(df, mapping={})
    assert list(out.columns) == ["x", "y"]
    assert out["y"].is_monotonic_increasing
    assert math.isclose(float(out["y"].iloc[-1]), 1.0)


def test_stat_sum_counts_duplicates():
    df = pd.DataFrame({"x": ["a", "a", "b"], "y": [1, 1, 2]})
    out = stat_sum().compute(df, mapping={})
    assert "n" in out.columns
    assert int(out.loc[(out["x"] == "a") & (out["y"] == 1), "n"].iloc[0]) == 2


def test_stat_qq_outputs_expected_columns():
    df = pd.DataFrame({"sample": [0.1, 0.2, 0.3, 0.4]})
    out = stat_qq().compute(df, mapping={})
    assert set(out.columns) == {"x", "y"}
    assert len(out) == 4


def test_stat_qq_line_outputs_two_points():
    df = pd.DataFrame({"sample": [0.1, 0.2, 0.3, 0.4]})
    out = stat_qq_line().compute(df, mapping={})
    assert set(out.columns) == {"x", "y"}
    assert len(out) == 2


def test_stat_bin2d_produces_fill_count():
    df = pd.DataFrame({"x": [0, 0, 1, 1], "y": [0, 1, 0, 1]})
    out = stat_bin2d(bins=2).compute(df, mapping={})
    assert {"x", "y", "count", "fill"}.issubset(out.columns)
    assert out["count"].sum() == 4


def test_stat_hull_can_drive_geom_line():
    df = pd.DataFrame({"x": [0, 1, 1, 0], "y": [0, 0, 1, 1]})
    hull = stat_hull().compute(df, mapping={})
    fig = (ggplot(hull, aes("x", "y")) + geom_line() + geom_point()).draw()
    assert len(fig.data) == 2


def test_stat_quantile_produces_multiple_quantiles():
    df = pd.DataFrame({"x": [0, 1, 2, 3], "y": [0, 0, 10, 10]})
    out = stat_quantile(quantiles=(0.25, 0.75), n=10).compute(df, mapping={})
    assert {"x", "y", "quantile"}.issubset(out.columns)
    assert set(out["quantile"].unique()) == {0.25, 0.75}


def test_stat_smooth_supports_lowess():
    df = pd.DataFrame({"x": [0, 1, 2, 3, 4], "y": [0, 1, 0, 1, 0]})
    out = stat_smooth(method="lowess").compute(df, mapping={})
    assert {"x", "y"}.issubset(out.columns)
    assert len(out) > 10
