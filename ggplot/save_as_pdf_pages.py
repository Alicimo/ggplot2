from __future__ import annotations

from pathlib import Path
from typing import Any

from .ggsave import ggsave


def save_as_pdf_pages(
    plots: list[Any],
    filename: str | Path,
    *,
    width: int = 700,
    height: int = 500,
):
    """Save a list of plots as individual pages.

    Plotly doesn't easily multiplex multiple figures into a single PDF without
    additional tooling; this minimal implementation saves numbered PDFs.
    """

    path = Path(filename)
    stem = path.stem
    suffix = ".pdf"
    for i, p in enumerate(plots, start=1):
        out = path.with_name(f"{stem}-{i}{suffix}")
        ggsave(out, p, width=width, height=height)
