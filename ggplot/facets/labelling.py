from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


def label_value(value: Any) -> str:
    return str(value)


def label_context(value: Any) -> str:
    return str(value)


def label_both(name: str, value: Any) -> str:
    return f"{name}: {value}"


@dataclass(frozen=True)
class labeller:
    func: Callable[..., str] | None = None

    def __call__(self, name: str, value: Any) -> str:
        if self.func is None:
            return label_both(name, value)
        return self.func(name, value)


def as_labeller(func: Callable[..., str]) -> labeller:
    return labeller(func=func)


def facet_null():
    # In plotnine this removes faceting; our default is effectively facet_null.
    from .facet import facet

    return facet()
