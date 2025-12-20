import pandas as pd

from ggplot import (
    aes,
    after_stat,
    facet_wrap,
    geom_area,
    geom_bar,
    geom_histogram,
    geom_path,
    geom_point,
    geom_rect,
    geom_ribbon,
    geom_segment,
    geom_text,
    geom_vline,
    ggplot,
    ggsave,
    scale_color_manual,
    scale_fill_manual,
    scale_x_continuous,
)


def test_basic_draw_and_save(tmp_path):
    df = pd.DataFrame(
        {
            "x": [1, 2, 3, 1, 2, 3],
            "y": [2, 3, 5, 2, 3, 4],
            "g": ["a", "a", "a", "b", "b", "b"],
        }
    )
    p = (
        ggplot(df, aes("x", "y"))
        + geom_point()
        + facet_wrap("g", ncol=2)
        + scale_x_continuous(limits=(0, 10), breaks=[0, 5, 10])
    )
    fig = p.draw()
    assert len(fig.data) == 2

    out = tmp_path / "plot.png"
    ggsave(out, plot=p, width=300, height=200)
    assert out.exists()


def test_discrete_scales_and_stats():
    df = pd.DataFrame({"x": [1, 2, 3, 4], "y": [2, 3, 5, 4], "g": ["a", "a", "b", "b"]})
    fig = (
        ggplot(df, aes("x", "y", color="g"))
        + geom_point()
        + scale_color_manual({"a": "red", "b": "blue"})
    ).draw()
    assert len(fig.data) == 2

    df_bar = pd.DataFrame({"x": ["a", "a", "b"]})
    fig2 = (ggplot(df_bar, aes("x", y=after_stat("count"))) + geom_bar()).draw()
    assert list(fig2.data[0].y) == [2, 1]

    df_fill = pd.DataFrame(
        {"x": ["a", "a", "a", "b", "b"], "fill": ["u", "v", "u", "u", "v"]}
    )
    fig3 = (
        ggplot(df_fill, aes("x", fill="fill"))
        + geom_bar(position="stack")
        + scale_fill_manual({"u": "#ff0000", "v": "#0000ff"})
    ).draw()
    assert len(fig3.data) == 2


def test_geoms_smoke():
    assert (
        len(
            (
                ggplot(pd.DataFrame({"x": [0, 1, 2], "y": [0, 1, 0]}), aes("x", "y"))
                + geom_path()
            )
            .draw()
            .data
        )
        == 1
    )
    assert (
        len(
            (
                ggplot(
                    pd.DataFrame({"x": [0], "y": [0], "xend": [1], "yend": [1]}),
                    aes("x", "y", xend="xend", yend="yend"),
                )
                + geom_segment()
            )
            .draw()
            .data
        )
        == 1
    )
    assert (
        len(
            (
                ggplot(
                    pd.DataFrame({"x": [0], "y": [0], "label": ["hi"]}),
                    aes("x", "y", label="label"),
                )
                + geom_text()
            )
            .draw()
            .data
        )
        == 1
    )

    df = pd.DataFrame({"xmin": [0], "xmax": [1], "ymin": [0], "ymax": [1]})
    assert (
        len(
            (
                ggplot(df, aes(xmin="xmin", xmax="xmax", ymin="ymin", ymax="ymax"))
                + geom_rect()
            )
            .draw()
            .data
        )
        == 1
    )

    df = pd.DataFrame({"x": [0, 1, 2], "ymin": [0, 0, 0], "ymax": [1, 2, 1]})
    assert (
        len(
            (ggplot(df, aes("x", ymin="ymin", ymax="ymax")) + geom_ribbon()).draw().data
        )
        == 1
    )

    df = pd.DataFrame({"x": [0, 1, 2], "y": [1, 2, 1]})
    assert len((ggplot(df, aes("x", "y")) + geom_area()).draw().data) == 1

    fig = (
        ggplot(pd.DataFrame({"xintercept": [1, 2]}), aes(xintercept="xintercept"))
        + geom_vline()
    ).draw()
    assert len(fig.layout.shapes) == 2

    assert (
        len(
            (
                ggplot(pd.DataFrame({"x": [1, 1, 2, 3, 3, 3]}), aes("x"))
                + geom_histogram(bins=3)
            )
            .draw()
            .data
        )
        == 1
    )
