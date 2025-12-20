import pandas as pd

from ggplot import aes, geom_point, ggplot


def test_horizontal_composition_or_operator():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
    p1 = ggplot(df, aes("x", "y")) + geom_point()
    p2 = ggplot(df, aes("x", "y")) + geom_point()
    fig = (p1 | p2).draw()
    assert len(fig.data) == 2


def test_vertical_composition_div_operator():
    df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
    p1 = ggplot(df, aes("x", "y")) + geom_point()
    p2 = ggplot(df, aes("x", "y")) + geom_point()
    fig = (p1 / p2).draw()
    assert len(fig.data) == 2
