import pandas as pd

from ggplot import aes, geom_point, ggplot, position_jitter, position_nudge


def test_position_nudge_shifts_points():
    df = pd.DataFrame({"x": [0.0], "y": [0.0]})
    p = ggplot(df, aes("x", "y")) + geom_point(position=position_nudge(x=1.0, y=2.0))
    built = p.build()
    layer_df = built.layers_data[0]
    assert float(layer_df["x"].iloc[0]) == 1.0
    assert float(layer_df["y"].iloc[0]) == 2.0


def test_position_jitter_changes_values():
    df = pd.DataFrame({"x": [0.0, 0.0], "y": [0.0, 0.0]})
    p = ggplot(df, aes("x", "y")) + geom_point(
        position=position_jitter(width=0.5, height=0.5, seed=1)
    )
    built = p.build()
    layer_df = built.layers_data[0]
    assert not (layer_df["x"] == 0.0).all() or not (layer_df["y"] == 0.0).all()
