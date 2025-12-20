Compat tests are adapted from the vendored upstream plotnine test suite.

Rules:
- No matplotlib image comparisons.
- Assertions target Plotly figures, build artifacts, and dataframe outputs.
- Only test features that exist (or that we are actively implementing).
