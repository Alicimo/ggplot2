import pandas as pd

from ggplot import aes, geom_point, ggplot, ggtitle, lims, xlab, xlim, ylab, ylim


def test_ggtitle_and_axis_labels_apply():
    df = pd.DataFrame({"x": [1, 2], "y": [1, 4]})
    fig = (
        ggplot(df, aes("x", "y"))
        + geom_point()
        + ggtitle("hello")
        + xlab("X")
        + ylab("Y")
    ).draw()
    assert fig.layout.title.text == "hello"
    assert fig.layout.xaxis.title.text == "X"
    assert fig.layout.yaxis.title.text == "Y"


def test_lims_sets_axis_ranges():
    df = pd.DataFrame({"x": [1, 2], "y": [1, 4]})
    fig = (ggplot(df, aes("x", "y")) + geom_point() + lims(x=(0, 3), y=(0, 5))).draw()
    assert tuple(fig.layout.xaxis.range) == (0, 3)
    assert tuple(fig.layout.yaxis.range) == (0, 5)


def test_xlim_ylim_helpers():
    df = pd.DataFrame({"x": [1, 2], "y": [1, 4]})
    fig = (ggplot(df, aes("x", "y")) + geom_point() + xlim(0, 3) + ylim(0, 5)).draw()
    assert tuple(fig.layout.xaxis.range) == (0, 3)
    assert tuple(fig.layout.yaxis.range) == (0, 5)
