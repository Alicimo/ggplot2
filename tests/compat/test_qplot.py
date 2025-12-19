import pandas as pd

from ggplot import qplot


def test_qplot_point_draws():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 4, 9]})
    fig = qplot('x', 'y', data=df, geom='point').draw()
    assert len(fig.data) == 1


def test_qplot_bar_draws():
    df = pd.DataFrame({'x': ['a', 'a', 'b']})
    fig = qplot('x', data=df, geom='bar').draw()
    assert len(fig.data) == 1

