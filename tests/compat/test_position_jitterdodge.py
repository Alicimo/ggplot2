import pandas as pd

from ggplot import aes, geom_point, ggplot, position_jitterdodge


def test_position_jitterdodge_moves_x():
    df = pd.DataFrame(
        {
            "x": ["a", "a", "b", "b"],
            "y": [0.0, 0.0, 0.0, 0.0],
            "fill": ["u", "v", "u", "v"],
        }
    )
    p = ggplot(df, aes("x", "y", fill="fill")) + geom_point(
        position=position_jitterdodge(seed=1, jitter_width=0.1)
    )
    built = p.build()
    layer_df = built.layers_data[0]
    # should no longer be purely categorical
    assert layer_df["x"].dtype.kind in ("f", "i")
