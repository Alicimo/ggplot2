import pandas as pd

from ggplot import aes, geom_errorbar, geom_linerange, ggplot


def test_geom_linerange_draws():
    df = pd.DataFrame({"x": [1, 2], "ymin": [0, 1], "ymax": [1, 2]})
    fig = (ggplot(df, aes("x", ymin="ymin", ymax="ymax")) + geom_linerange()).draw()
    assert len(fig.data) == 1


def test_geom_errorbar_draws():
    df = pd.DataFrame({"x": [1, 2], "ymin": [0, 1], "ymax": [1, 2]})
    fig = (
        ggplot(df, aes("x", ymin="ymin", ymax="ymax")) + geom_errorbar(width=0.2)
    ).draw()
    assert len(fig.data) == 1
