import pandas as pd

from ggplot import aes, geom_bar, ggplot


def test_position_stack_produces_ymin_ymax():
    df = pd.DataFrame(
        {"x": ["a", "a", "a", "b", "b"], "fill": ["u", "v", "u", "u", "v"]}
    )
    p = ggplot(df, aes("x", fill="fill")) + geom_bar(position="stack")
    built = p.build()
    layer_df = built.layers_data[0]
    assert "ymin" in layer_df.columns
    assert "ymax" in layer_df.columns


def test_position_dodge_offsets_x_numeric():
    df = pd.DataFrame(
        {"x": ["a", "a", "b", "b"], "fill": ["u", "v", "u", "v"], "y": [1, 1, 1, 1]}
    )
    # Use identity stat and dodge via explicit position object.
    from ggplot.geoms.geom_bar import geom_bar as geom_bar_factory

    g = geom_bar_factory(stat="identity", position="dodge")
    p = ggplot(df, aes("x", "y", fill="fill")) + g
    built = p.build()
    layer_df = built.layers_data[0]
    assert layer_df["x"].dtype.kind in ("f", "i")
