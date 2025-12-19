import pandas as pd

from ggplot import aes, geom_polygon, geom_tile, ggplot


def test_geom_tile_heatmap():
    df = pd.DataFrame({'x': ['a', 'b'], 'y': ['c', 'c'], 'fill': [1, 2]})
    fig = (ggplot(df, aes('x', 'y', fill='fill')) + geom_tile()).draw()
    assert len(fig.data) == 1
    assert fig.data[0].type == 'heatmap'


def test_geom_polygon_draws():
    df = pd.DataFrame({'x': [0, 1, 1, 0], 'y': [0, 0, 1, 1], 'group': [1, 1, 1, 1]})
    fig = (ggplot(df, aes('x', 'y', group='group')) + geom_polygon()).draw()
    assert len(fig.data) == 1

