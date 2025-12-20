import pandas as pd

from ggplot import aes, geom_density, ggplot


def test_geom_density_draws():
    df = pd.DataFrame({"y": [1, 2, 3, 4, 5]})
    fig = (ggplot(df, aes(y="y")) + geom_density()).draw()
    assert len(fig.data) == 1
    assert fig.data[0].mode == "lines"
