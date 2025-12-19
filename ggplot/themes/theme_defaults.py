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

