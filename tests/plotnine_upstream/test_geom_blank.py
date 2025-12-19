from ggplot import aes, geom_blank, ggplot
from ggplot.data import mtcars


def test_blank():
    gg = ggplot(mtcars, aes(x="wt", y="mpg"))
    gg = gg + geom_blank()
    assert gg == "blank"
