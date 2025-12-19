import pandas as pd

from ggplot import aes, geom_col, ggplot


def test_geom_col_identity_bar_heights():
    df = pd.DataFrame({'x': ['a', 'b'], 'y': [2, 5]})
    fig = (ggplot(df, aes('x', 'y')) + geom_col()).draw()
    assert list(fig.data[0].y) == [2, 5]

