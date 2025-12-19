import pandas as pd

from ggplot import aes, geom_dotplot, ggplot


def test_geom_dotplot_draws_markers():
    df = pd.DataFrame({'x': [1, 2, 3]})
    fig = (ggplot(df, aes('x')) + geom_dotplot()).draw()
    assert len(fig.data) == 1
    assert fig.data[0].mode == 'markers'

