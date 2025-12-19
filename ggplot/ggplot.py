from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import Any, Optional

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from ._utils.data import as_data_frame
from .exceptions import PlotAddError
from .layers import Layers
from .mapping.aes import aes
from .typing import DataLike, PlotAddable
from .facets.facet_null import facet_null


class ggplot:
    """Create a new ggplot object.

    Phase 0: stores data + mapping and supports the additive API.
    Rendering/build pipeline is added in later phases.
    """

    def __init__(self, data: Optional[DataLike] = None, mapping: Optional[aes] = None):
        self.data: pd.DataFrame = as_data_frame(data)
        self.mapping: aes = mapping if mapping is not None else aes()

        # Future components (facets/scales/theme/guides/coords) will live here.
        self.layers: Layers = Layers()
        self.labels: dict[str, str] = {}
        self.theme: dict[str, Any] = {}
        self.scales: list[Any] = []
        self.facet: Any = facet_null()

    def __iadd__(self, other: PlotAddable | list[PlotAddable] | None):
        if other is None:
            return self
        if isinstance(other, list):
            for item in other:
                item.__radd__(self)
            return self
        other.__radd__(self)
        return self

    def __add__(self, rhs: PlotAddable | list[PlotAddable] | None) -> "ggplot":
        p = deepcopy(self)
        return p.__iadd__(rhs)

    def __radd__(self, other: Any) -> "ggplot":
        raise PlotAddError(f"Cannot add ggplot to {type(other)!r}")

    @dataclass(frozen=True)
    class Built:
        plot: "ggplot"
        layers_data: list[pd.DataFrame]

    def build(self) -> "ggplot.Built":
        plot_data = self.data
        layers_data: list[pd.DataFrame] = []
        for lyr in self.layers:
            df = lyr.setup_data(plot_data)
            df = lyr.resolve_mapping(df, plot_mapping=self.mapping)
            df = lyr.stat.compute(df, mapping=dict(lyr.mapping))
            df = lyr.position.adjust(df)
            layers_data.append(df)
        return ggplot.Built(plot=self, layers_data=layers_data)

    def draw(self) -> go.Figure:
        built = self.build()

        # Faceting (v0: facet_null or facet_wrap on a single variable)
        # We facet based on the plot data only (layers with their own data are
        # still rendered in each panel if they carry the facet column).
        panels = self.facet.get_panels(self.data)
        n_panels = len(panels)
        nrow, ncol = (1, 1)
        if hasattr(self.facet, "layout"):
            nrow, ncol = self.facet.layout(n_panels)

        fig = make_subplots(rows=nrow, cols=ncol, subplot_titles=[t for t, _ in panels])
        for pidx, (_, panel_df) in enumerate(panels):
            row = pidx // ncol + 1
            col = pidx % ncol + 1
            for lyr, layer_df in zip(self.layers, built.layers_data, strict=False):
                # If layer data includes the facet column, filter to this panel.
                df = layer_df
                facet_col = getattr(self.facet, "facets", None)
                if facet_col and facet_col in df.columns and facet_col in panel_df.columns:
                    key = panel_df[facet_col].iloc[0] if not panel_df.empty else None
                    df = df[df[facet_col] == key]

                geom = lyr.geom
                to_traces = getattr(geom, "to_traces", None)
                if callable(to_traces):
                    for trace in to_traces(df, plot=self):
                        fig.add_trace(trace, row=row, col=col)

        if title := self.labels.get("title"):
            fig.update_layout(title=title)
        if x := self.labels.get("x"):
            fig.update_xaxes(title_text=x)
        if y := self.labels.get("y"):
            fig.update_yaxes(title_text=y)

        # Theme (v0): map a few common knobs to Plotly layout
        if self.theme:
            layout_updates = {}
            axis_updates_x = {}
            axis_updates_y = {}
            if "plot_bgcolor" in self.theme:
                layout_updates["plot_bgcolor"] = self.theme["plot_bgcolor"]
            if "paper_bgcolor" in self.theme:
                layout_updates["paper_bgcolor"] = self.theme["paper_bgcolor"]
            if "gridcolor" in self.theme:
                axis_updates_x["gridcolor"] = self.theme["gridcolor"]
                axis_updates_y["gridcolor"] = self.theme["gridcolor"]
            if "xaxis_showgrid" in self.theme:
                axis_updates_x["showgrid"] = self.theme["xaxis_showgrid"]
            if "yaxis_showgrid" in self.theme:
                axis_updates_y["showgrid"] = self.theme["yaxis_showgrid"]
            if layout_updates:
                fig.update_layout(**layout_updates)
            if axis_updates_x:
                fig.update_xaxes(**axis_updates_x)
            if axis_updates_y:
                fig.update_yaxes(**axis_updates_y)

        # Apply trained scales (v0: only x/y continuous limits and breaks).
        for s in getattr(self, "scales", []):
            if getattr(s, "aesthetic", None) == "x":
                xdomain = None
                for df in built.layers_data:
                    if "x" in df.columns:
                        xdomain = s.train(df["x"]) if xdomain is None else (
                            min(xdomain[0], s.train(df["x"])[0]),
                            max(xdomain[1], s.train(df["x"])[1]),
                        )
                if xdomain is not None:
                    fig.update_xaxes(range=list(xdomain))
                if getattr(s, "breaks", None) is not None:
                    fig.update_xaxes(tickmode="array", tickvals=list(s.breaks))
            if getattr(s, "aesthetic", None) == "y":
                ydomain = None
                for df in built.layers_data:
                    if "y" in df.columns:
                        ydomain = s.train(df["y"]) if ydomain is None else (
                            min(ydomain[0], s.train(df["y"])[0]),
                            max(ydomain[1], s.train(df["y"])[1]),
                        )
                if ydomain is not None:
                    fig.update_yaxes(range=list(ydomain))
                if getattr(s, "breaks", None) is not None:
                    fig.update_yaxes(tickmode="array", tickvals=list(s.breaks))
        return fig

    def to_plotly(self) -> go.Figure:
        return self.draw()
