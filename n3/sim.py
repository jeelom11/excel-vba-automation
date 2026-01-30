"""Simulation helpers for draws."""

from __future__ import annotations

import random
from typing import Iterable

from .ev import Outcome


def simulate_draws(outcomes: Iterable[Outcome], draws: int, *, seed: int | None = None) -> list[Outcome]:
    outcomes_list = list(outcomes)
    if draws <= 0:
        raise ValueError("Draws must be positive.")
    if not outcomes_list:
        raise ValueError("At least one outcome is required to simulate draws.")

    rng = random.Random(seed)
    weights = [outcome.sales for outcome in outcomes_list]
    return rng.choices(outcomes_list, weights=weights, k=draws)
