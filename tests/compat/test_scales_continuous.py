import pandas as pd

from ggplot import (
    aes,
    geom_point,
    geom_tile,
    ggplot,
    scale_color_continuous,
    scale_fill_gradient,
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
