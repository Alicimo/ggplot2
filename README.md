# ggplot2

Work-in-progress: a Plotly-backed port of plotnine with an API inspired by ggplot2.

Import namespace: `ggplot`

## Quickstart

```python
import pandas as pd
from ggplot import (
    ggplot,
    aes,
    geom_point,
    geom_line,
    geom_bar,
    geom_histogram,
    labs,
    facet_wrap,
    theme_minimal,
    scale_x_continuous,
    scale_color_manual,
    scale_fill_manual,
    ggsave,
)

df = pd.DataFrame({
    'x': [1, 2, 3, 1, 2, 3],
    'y': [2, 3, 5, 2, 3, 4],
    'g': ['a', 'a', 'a', 'b', 'b', 'b'],
})

p = (
    ggplot(df, aes('x', 'y', color='g'))
    + geom_point()
    + geom_line()
    + labs(title='Example', x='X', y='Y')
    + theme_minimal()
    + facet_wrap('g', ncol=2)
    + scale_x_continuous(limits=(0, 4), breaks=[0, 2, 4])
    + scale_color_manual({'a': 'red', 'b': 'blue'})
)

fig = p.draw()
fig.show()

ggsave('plot.png', plot=p, width=800, height=500)
```
