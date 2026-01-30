"""Risk and summary metrics."""

from __future__ import annotations

from typing import Iterable


def mean(values: Iterable[float]) -> float:
    values_list = list(values)
    if not values_list:
        raise ValueError("Values must be non-empty.")
    return sum(values_list) / len(values_list)


def variance(values: Iterable[float]) -> float:
    values_list = list(values)
    if len(values_list) < 2:
        raise ValueError("At least two values are required to compute variance.")
    avg = mean(values_list)
    return sum((value - avg) ** 2 for value in values_list) / (len(values_list) - 1)
