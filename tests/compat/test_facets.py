import pandas as pd

from ggplot import aes, facet_wrap, geom_point, ggplot


def test_facet_wrap_creates_multiple_panels():
    df = pd.DataFrame({'x': [1, 2, 1, 2], 'y': [1, 2, 2, 1], 'g': ['a', 'a', 'b', 'b']})
    p = ggplot(df, aes('x', 'y')) + geom_point() + facet_wrap('g', ncol=2)
    fig = p.draw()
    assert len(fig.data) == 2
    # subplot titles
    assert len(fig.layout.annotations) >= 2

