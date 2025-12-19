class GGPlotError(Exception):
    """Base exception for ggplot."""


class MappingError(GGPlotError):
    """Raised for invalid aesthetic mappings."""


class PlotAddError(GGPlotError):
    """Raised when an object cannot be added to a ggplot."""

