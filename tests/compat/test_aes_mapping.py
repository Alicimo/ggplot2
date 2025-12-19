import pandas as pd
import pytest

from ggplot import aes, after_stat, geom_bar, geom_point, ggplot
from ggplot.exceptions import MappingError


def test_aes_column_mapping():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 5]})
    p = ggplot(df, aes('x', 'y')) + geom_point()
    fig = p.draw()
    assert len(fig.data) == 1


def test_aes_expression_mapping():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [2, 3, 5]})
    p = ggplot(df, aes('x', 'y*2')) + geom_point()
    fig = p.draw()
    assert list(fig.data[0].y) == [4, 6, 10]


def test_aes_unknown_identifier_is_error():
    df = pd.DataFrame({'x': [1, 2, 3]})
    with pytest.raises(MappingError):
        (ggplot(df, aes('missing_col')) + geom_point()).draw()


def test_after_stat_evaluates_post_stat():
    df = pd.DataFrame({'x': ['a', 'a', 'b']})
    p = ggplot(df, aes('x', y=after_stat('count'))) + geom_bar()
    fig = p.draw()
    assert list(fig.data[0].y) == [2, 1]
