import pandas as pd

from ggplot import aes, after_stat, geom_bar, geom_histogram, ggplot


def test_stat_count_via_geom_bar():
    df = pd.DataFrame({"x": ["a", "a", "b"]})
    p = ggplot(df, aes("x", y=after_stat("count"))) + geom_bar()
    fig = p.draw()
    assert list(fig.data[0].x) == ["a", "b"]
    assert list(fig.data[0].y) == [2, 1]


def test_stat_bin_via_geom_histogram():
    df = pd.DataFrame({"x": [1, 1, 2, 3, 3, 3]})
    p = ggplot(df, aes("x")) + geom_histogram(bins=3)
    fig = p.draw()
    assert len(fig.data) == 1
    assert fig.data[0].type == "bar"
