import pandas as pd

from ggplot import aes, geom_boxplot, ggplot


def test_geom_boxplot_builds_stats():
    df = pd.DataFrame({'x': ['a'] * 5 + ['b'] * 5, 'y': [1, 2, 3, 4, 5, 2, 2, 3, 3, 4]})
    p = ggplot(df, aes('x', 'y')) + geom_boxplot()
    built = p.build()
    layer_df = built.layers_data[0]
    assert set(['lower', 'middle', 'upper', 'ymin', 'ymax']).issubset(layer_df.columns)

