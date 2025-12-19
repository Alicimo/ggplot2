import pandas as pd

from ggplot import aes, geom_rug, ggplot


def test_geom_rug_adds_shapes():
    df = pd.DataFrame({'x': [1, 2, 3]})
    fig = (ggplot(df, aes('x')) + geom_rug()).draw()
    assert len(fig.layout.shapes) == 3

