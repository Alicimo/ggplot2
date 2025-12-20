from __future__ import annotations

from pathlib import Path
from typing import Any

import plotly.graph_objects as go

from .exceptions import GGPlotError


def ggsave(
    filename: str | Path,
    *,
    plot: Any,
    width: int | None = None,
    height: int | None = None,
    scale: float = 1.0,
) -> Path:
    """Save a plot to an image file using Plotly + Kaleido.

    Parameters
    ----------
    filename:
        Output file path. Extension determines format (png, jpg/jpeg, svg, pdf, ...).
    plot:
        A `ggplot` instance or a Plotly Figure.
    width, height:
        Pixel dimensions for raster formats.
    scale:
        Scale factor for the exported image.
    """

    path = Path(filename)
    if isinstance(plot, go.Figure):
        fig = plot
    elif hasattr(plot, "to_plotly"):
        fig = plot.to_plotly()
    elif hasattr(plot, "draw"):
        fig = plot.draw()
    else:
        raise GGPlotError(f"Unsupported plot type for ggsave: {type(plot)!r}")

    # Requires kaleido at runtime.
    fig.write_image(str(path), width=width, height=height, scale=scale)
    return path
