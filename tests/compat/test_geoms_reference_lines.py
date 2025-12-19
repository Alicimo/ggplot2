import pandas as pd

from ggplot import aes, geom_abline, geom_hline, ggplot


def test_geom_hline_adds_shapes():
    df = pd.DataFrame({'yintercept': [1, 2]})
    fig = (ggplot(df, aes(yintercept='yintercept')) + geom_hline()).draw()
    assert len(fig.layout.shapes) == 2


def test_geom_abline_adds_shapes():
    df = pd.DataFrame({'intercept': [0], 'slope': [1]})
    fig = (ggplot(df, aes(intercept='intercept', slope='slope')) + geom_abline()).draw()
    assert len(fig.layout.shapes) == 1

