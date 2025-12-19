import pandas as pd

from ggplot import aes, coord_flip, facet_grid, geom_point, ggplot


def test_coord_flip_draws():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 5]})
    fig = (ggplot(df, aes('x', 'y')) + geom_point() + coord_flip()).draw()
    assert len(fig.data) == 1


def test_facet_grid_creates_panels():
    df = pd.DataFrame({'x': [1, 2, 1, 2], 'y': [1, 2, 2, 1], 'r': ['a', 'a', 'b', 'b'], 'c': ['u', 'v', 'u', 'v']})
    fig = (ggplot(df, aes('x', 'y')) + geom_point() + facet_grid(rows='r', cols='c')).draw()
    # 4 panels => 4 traces
    assert len(fig.data) == 4

