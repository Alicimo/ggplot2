import pandas as pd

from ggplot import aes, geom_smooth, ggplot


def test_geom_smooth_draws_line():
    df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [2, 3, 5, 4]})
    fig = (ggplot(df, aes('x', 'y')) + geom_smooth()).draw()
    assert len(fig.data) == 1
    assert fig.data[0].mode == 'lines'

