from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

import plotly.graph_objects as go
from plotly.subplots import make_subplots


@dataclass
class Compose:
    plots: list
    direction: str  # 'h' or 'v'

    def __or__(self, rhs):
        return Compose([*self.plots, rhs], direction="h")

    def __truediv__(self, rhs):
        return Compose([*self.plots, rhs], direction="v")

    def draw(self) -> go.Figure:
        n = len(self.plots)
        if self.direction == "h":
            fig = make_subplots(rows=1, cols=n)
            for i, p in enumerate(self.plots, start=1):
                sub = p.draw() if hasattr(p, "draw") else p
                for trace in sub.data:
                    fig.add_trace(trace, row=1, col=i)
            return fig
        fig = make_subplots(rows=n, cols=1)
        for i, p in enumerate(self.plots, start=1):
            sub = p.draw() if hasattr(p, "draw") else p
            for trace in sub.data:
                fig.add_trace(trace, row=i, col=1)
        return fig


def _as_plot_list(items) -> list:
    if isinstance(items, Sequence) and not isinstance(items, (str, bytes)):
        return list(items)
    return [items]

