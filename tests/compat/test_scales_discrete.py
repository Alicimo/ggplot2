import pandas as pd

from ggplot import aes, geom_point, ggplot, scale_x_discrete


def test_scale_x_discrete_orders_categories():
    df = pd.DataFrame({'x': ['b', 'a', 'c'], 'y': [1, 2, 3]})
    fig = (ggplot(df, aes('x', 'y')) + geom_point() + scale_x_discrete(limits=['a', 'b', 'c'])).draw()
    assert list(fig.layout.xaxis.categoryarray) == ['a', 'b', 'c']

