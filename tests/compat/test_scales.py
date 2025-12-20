import pandas as pd

from ggplot import aes, geom_point, ggplot, scale_x_continuous, scale_y_continuous


def test_scale_x_limits_and_breaks_apply_to_figure():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [2, 3, 5]})
    p = (
        ggplot(df, aes("x", "y"))
        + geom_point()
        + scale_x_continuous(limits=(0, 10), breaks=[0, 5, 10])
    )
    fig = p.draw()
    assert list(fig.layout.xaxis.range) == [0, 10]
    assert list(fig.layout.xaxis.tickvals) == [0, 5, 10]


def test_scale_y_limits_apply_to_figure():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [2, 3, 5]})
    p = ggplot(df, aes("x", "y")) + geom_point() + scale_y_continuous(limits=(0, 6))
    fig = p.draw()
    assert list(fig.layout.yaxis.range) == [0, 6]
