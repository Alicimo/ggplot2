from __future__ import annotations

import ast
from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np
import pandas as pd

from ..exceptions import MappingError


@dataclass(frozen=True)
class after_stat:
    expr: str


def _safe_eval_expr(expr: str, df: pd.DataFrame, env: Mapping[str, Any]) -> Any:
    """Evaluate a restricted python expression against a dataframe.

    Allowed:
    - Names: dataframe columns, plus keys from env
    - Literals
    - Arithmetic: + - * / ** %
    - Comparisons: < <= > >= == !=
    - Boolean ops: & | and/or (via ast BoolOp)
    - Unary ops: + - ~

    Not allowed:
    - attribute access (a.b)
    - function calls
    - subscripting (a[0])

    This is intentionally conservative for v0.
    """

    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise MappingError(f"Invalid expression: {expr!r}") from e

    allowed_nodes = (
        ast.Expression,
        ast.BinOp,
        ast.UnaryOp,
        ast.BoolOp,
        ast.Compare,
        ast.Name,
        ast.Load,
        ast.Constant,
        ast.And,
        ast.Or,
        ast.Add,
        ast.Sub,
        ast.Mult,
        ast.Div,
        ast.Mod,
        ast.Pow,
        ast.USub,
        ast.UAdd,
        ast.Invert,
        ast.Eq,
        ast.NotEq,
        ast.Lt,
        ast.LtE,
        ast.Gt,
        ast.GtE,
        ast.BitAnd,
        ast.BitOr,
    )

    for node in ast.walk(tree):
        if not isinstance(node, allowed_nodes):
            raise MappingError(
                f"Unsupported expression syntax in {expr!r}: {node.__class__.__name__}"
            )
        if isinstance(node, ast.Name) and node.id.startswith("__"):
            raise MappingError("Invalid name in expression")

    code = compile(tree, filename="<aes-expr>", mode="eval")

    scope: dict[str, Any] = {"np": np}
    scope.update(env)
    for col in df.columns:
        scope[col] = df[col]

    return eval(code, {"__builtins__": {}}, scope)


def evaluate_mapping_value(
    value: Any,
    df: pd.DataFrame,
    *,
    env: Mapping[str, Any] | None = None,
) -> Any:
    """Resolve a mapping value against a dataframe.

    - If value is after_stat(expr): return a callable marker to be resolved later.
    - If value is a string:
        - column name -> df[col]
        - otherwise treated as expression
    - Otherwise returned as-is (scalars/arrays handled by downstream normalization)
    """

    if env is None:
        env = {}

    if isinstance(value, after_stat):
        return value

    if isinstance(value, str):
        if value in df.columns:
            return df[value]
        # If the value looks like an identifier but isn't a column/env name,
        # treat it as a missing column for friendlier errors.
        if value.isidentifier() and value not in env:
            raise MappingError(f"Unknown column in mapping: {value!r}")
        return _safe_eval_expr(value, df, env)

    return value
