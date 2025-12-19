from __future__ import annotations

from typing import Any

import pandas as pd

from ..exceptions import GGPlotError


def as_data_frame(data: Any) -> pd.DataFrame:
    """Coerce supported data inputs to a pandas DataFrame.

    Supported:
    - pandas.DataFrame
    - dict of columns
    - list of records
    - None -> empty DataFrame
    """

    if data is None:
        return pd.DataFrame()
    if isinstance(data, pd.DataFrame):
        # Avoid surprising mutations later in the pipeline.
        return data.copy(deep=False)
    if isinstance(data, dict):
        return pd.DataFrame(data)
    if isinstance(data, list):
        # list[dict] expected
        return pd.DataFrame.from_records(data)
    raise GGPlotError(f"Unsupported data type: {type(data)!r}")
