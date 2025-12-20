from __future__ import annotations

from .theme import theme


def theme_minimal() -> theme:
    return theme(
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis_showgrid=True,
        yaxis_showgrid=True,
        gridcolor="#E5E5E5",
    )


def theme_void() -> theme:
    return theme(
        plot_bgcolor="white",
        paper_bgcolor="white",
        xaxis_showgrid=False,
        yaxis_showgrid=False,
    )


def theme_gray() -> theme:
    return theme_minimal()


def theme_grey() -> theme:
    return theme_gray()


def theme_bw() -> theme:
    return theme_minimal()


def theme_classic() -> theme:
    return theme_minimal()


def theme_dark() -> theme:
    return theme(plot_bgcolor="#1e1e1e", paper_bgcolor="#1e1e1e")


def theme_light() -> theme:
    return theme_minimal()


def theme_linedraw() -> theme:
    return theme_minimal()


def theme_matplotlib() -> theme:
    return theme_minimal()


def theme_seaborn() -> theme:
    return theme_minimal()


def theme_tufte() -> theme:
    return theme_void()


def theme_xkcd() -> theme:
    return theme_minimal()


def theme_538() -> theme:
    return theme_minimal()
