import pandas as pd

from ggplot import (
    aes,
    geom_area,
    geom_point,
    geom_ribbon,
    geom_tile,
    ggplot,
    scale_alpha_continuous,
    scale_color_continuous,
    scale_fill_gradient,
    scale_size_continuous,
)


def test_scale_color_continuous_produces_colorscale_marker():
    df = pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0], "c": [0.0, 0.5, 1.0]})
    fig = (
        ggplot(df, aes("x", "y", color="c")) + geom_point() + scale_color_continuous()
    ).draw()
    assert len(fig.data) == 1
    assert fig.data[0].type == "scatter"
    assert fig.data[0].marker.showscale is True


def test_scale_fill_gradient_applies_to_tile_heatmap():
    df = pd.DataFrame({"x": ["a", "b"], "y": ["c", "c"], "fill": [0.0, 1.0]})
    fig = (
        ggplot(df, aes("x", "y", fill="fill"))
        + geom_tile()
        + scale_fill_gradient(low="#000000", high="#ffffff")
    ).draw()
    assert len(fig.data) == 1
    assert fig.data[0].type == "heatmap"
    assert fig.data[0].showscale is True


def test_alpha_applies_to_point_marker_opacity():
    df = pd.DataFrame({"x": [0, 1], "y": [0, 1], "alpha": [0.2, 0.8]})
    fig = (
        ggplot(df, aes("x", "y", alpha="alpha"))
        + geom_point()
        + scale_alpha_continuous(range=(0.0, 1.0))
    ).draw()
    assert fig.data[0].marker.opacity is not None


def test_scale_size_continuous_maps_to_marker_size():
    df = pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0], "s": [0.0, 0.5, 1.0]})
    fig = (
        ggplot(df, aes("x", "y", size="s"))
        + geom_point()
        + scale_size_continuous(range=(1.0, 9.0))
    ).draw()
    assert fig.data[0].marker.size is not None


def test_alpha_applies_to_area_and_ribbon_opacity():
    df = pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0], "alpha": [0.3, 0.3, 0.3]})
    fig = (ggplot(df, aes("x", "y", alpha="alpha")) + geom_area()).draw()
    assert fig.data[0].opacity == 0.3

    df2 = pd.DataFrame(
        {"x": [0, 1, 2], "ymin": [0, 0, 0], "ymax": [1, 2, 1], "alpha": [0.4, 0.4, 0.4]}
    )
    fig2 = (
        ggplot(df2, aes("x", ymin="ymin", ymax="ymax", alpha="alpha")) + geom_ribbon()
    ).draw()
    assert fig2.data[0].opacity == 0.4
