from __future__ import annotations

from typing import Any

_THEME_STACK: list[dict[str, Any]] = []


def theme_set(theme: dict[str, Any]):
    _THEME_STACK.clear()
    _THEME_STACK.append(dict(theme))


def theme_get() -> dict[str, Any] | None:
    return _THEME_STACK[-1] if _THEME_STACK else None


def theme_update(**kwargs: Any):
    current = theme_get()
    if current is None:
        theme_set(kwargs)
    else:
        current.update(kwargs)
