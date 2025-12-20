from __future__ import annotations

from .addables import labs


def ggtitle(title: str):
    return labs(title=title)


def xlab(label: str):
    return labs(x=label)


def ylab(label: str):
    return labs(y=label)
