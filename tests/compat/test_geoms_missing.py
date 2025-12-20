import pandas as pd

from ggplot import (
    aes,
    geom_bin2d,
    geom_blank,
    geom_count,
    geom_crossbar,
    geom_density_2d,
    geom_errorbarh,
    geom_freqpoly,
    geom_label,
    geom_map,
    geom_point,
    geom_pointdensity,
    geom_qq,
    geom_qq_line,
    geom_quantile,
    geom_raster,
    geom_sina,
    geom_spoke,
    geom_step,
    ggplot,
)


def test_geom_blank_draws_nothing():
    df = pd.DataFrame({"x": [1, 2], "y": [1, 2]})
    fig = (ggplot(df, aes("x", "y")) + geom_blank()).draw()
    assert len(fig.data) == 0


def test_geom_errorbarh_draws():
    df = pd.DataFrame({"y": [1, 2], "xmin": [0, 1], "xmax": [1, 2]})
    fig = (ggplot(df, aes(y="y", xmin="xmin", xmax="xmax")) + geom_errorbarh()).draw()
    assert len(fig.data) == 1


def test_geom_freqpoly_draws():
    df = pd.DataFrame({"x": [1, 1, 2, 2, 3]})
    fig = (ggplot(df, aes("x")) + geom_freqpoly(bins=3)).draw()
    assert len(fig.data) == 1


def test_geom_count_draws():
    df = pd.DataFrame({"x": ["a", "a", "b"], "y": [1, 1, 2]})
    fig = (ggplot(df, aes("x")) + geom_count()).draw()
    assert len(fig.data) == 1


def test_geom_raster_draws_heatmap():
    df = pd.DataFrame({"x": ["a", "b"], "y": ["c", "c"], "fill": [1, 2]})
    fig = (ggplot(df, aes("x", "y", fill="fill")) + geom_raster()).draw()
    assert len(fig.data) == 1
    assert fig.data[0].type == "heatmap"


def test_geom_bin2d_is_heatmap_alias():
    df = pd.DataFrame({"x": ["a", "b"], "y": ["c", "c"], "fill": [1, 2]})
    fig = (ggplot(df, aes("x", "y", fill="fill")) + geom_bin2d()).draw()
    assert len(fig.data) == 1
    assert fig.data[0].type == "heatmap"


def test_geom_density_2d_draws():
    df = pd.DataFrame({"x": [0, 1, 1, 0], "y": [0, 0, 1, 1], "group": [1, 1, 1, 1]})
    fig = (ggplot(df, aes("x", "y", group="group")) + geom_density_2d()).draw()
    assert len(fig.data) == 1


def test_geom_label_draws():
    df = pd.DataFrame({"x": [1, 2], "y": [1, 2], "label": ["a", "b"]})
    fig = (ggplot(df, aes("x", "y", label="label")) + geom_label()).draw()
    assert len(fig.data) == 1
    assert fig.data[0].mode == "markers+text"


def test_geom_map_is_polygon_alias():
    df = pd.DataFrame({"x": [0, 1, 1, 0], "y": [0, 0, 1, 1], "group": [1, 1, 1, 1]})
    fig = (ggplot(df, aes("x", "y", group="group")) + geom_map()).draw()
    assert len(fig.data) == 1


def test_geom_pointdensity_draws():
    df = pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0]})
    fig = (ggplot(df, aes("x", "y")) + geom_pointdensity()).draw()
    assert len(fig.data) == 1


def test_geom_qq_and_line_draw():
    df = pd.DataFrame({"sample": [0.1, 0.2, 0.3, 0.4, 0.5]})
    fig = (ggplot(df, aes(sample="sample")) + geom_qq() + geom_qq_line()).draw()
    assert len(fig.data) == 2


def test_geom_quantile_draws():
    df = pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0]})
    fig = (ggplot(df, aes("x", "y")) + geom_quantile()).draw()
    assert len(fig.data) == 1


def test_geom_sina_draws():
    df = pd.DataFrame({"x": [1, 1, 1, 1], "y": [0, 1, 2, 3]})
    fig = (ggplot(df, aes("x", "y")) + geom_sina(seed=1)).draw()
    assert len(fig.data) == 1
    assert fig.data[0].mode == "markers"


def test_geom_spoke_draws():
    df = pd.DataFrame(
        {"x": [0, 1], "y": [0, 0], "angle": [0.0, 1.57], "radius": [1.0, 1.0]}
    )
    fig = (
        ggplot(df, aes("x", "y", angle="angle", radius="radius")) + geom_spoke()
    ).draw()
    assert len(fig.data) == 1


def test_geom_step_draws():
    df = pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0]})
    fig = (ggplot(df, aes("x", "y")) + geom_step(direction="hv")).draw()
    assert len(fig.data) == 1


def test_geom_crossbar_draws():
    df = pd.DataFrame({"x": [1], "ymin": [0], "ymax": [2], "y": [1]})
    fig = (
        ggplot(df, aes("x", y="y", ymin="ymin", ymax="ymax")) + geom_crossbar()
    ).draw()
    assert len(fig.data) >= 2


def test_new_geoms_interop_with_existing():
    df = pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0]})
    fig = (ggplot(df, aes("x", "y")) + geom_point() + geom_step()).draw()
    assert len(fig.data) == 2
