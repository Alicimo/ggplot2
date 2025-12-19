import pandas as pd

from ggplot import aes, geom_jitter, ggplot


def test_geom_jitter_draws():
    df = pd.DataFrame({'x': [0.0, 0.0], 'y': [0.0, 0.0]})
    fig = (ggplot(df, aes('x', 'y')) + geom_jitter(seed=1)).draw()
    assert len(fig.data) == 1

