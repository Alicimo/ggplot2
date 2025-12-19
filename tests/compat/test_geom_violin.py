import pandas as pd

from ggplot import aes, geom_violin, ggplot


def test_geom_violin_draws():
    df = pd.DataFrame({'x': ['a'] * 20 + ['b'] * 20, 'y': list(range(20)) + list(range(20))})
    fig = (ggplot(df, aes('x', 'y')) + geom_violin()).draw()
    assert len(fig.data) >= 1

