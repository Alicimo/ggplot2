import pandas as pd

from ggplot import aes, ggplot, stat_summary, stat_summary_range


def test_stat_summary_mean_adds_points():
    df = pd.DataFrame({"x": ["a", "a", "b", "b"], "y": [1, 3, 2, 4]})
    fig = (ggplot(df, aes("x", "y")) + stat_summary(fun="mean")).draw()
    assert len(fig.data) == 1


def test_stat_summary_range_produces_error_bars():
    df = pd.DataFrame({"x": ["a", "a", "b", "b"], "y": [1, 3, 2, 4]})
    built = (ggplot(df, aes("x", "y")) + stat_summary_range()).build()
    layer_df = built.layers_data[0]
    assert set(["y", "ymin", "ymax"]).issubset(layer_df.columns)
