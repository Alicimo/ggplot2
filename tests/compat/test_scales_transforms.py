import pandas as pd

from ggplot import aes, geom_point, ggplot, scale_x_log10


def test_scale_x_log10_transforms_data():
    df = pd.DataFrame({"x": [1, 10, 100], "y": [1, 2, 3]})
    fig = (ggplot(df, aes("x", "y")) + geom_point() + scale_x_log10()).draw()
    assert list(fig.data[0].x) == [0.0, 1.0, 2.0]
