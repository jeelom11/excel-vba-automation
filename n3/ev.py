"""Expected value calculations for N3 ticket outcomes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Outcome:
    name: str
    sales: int
    payout: float


def total_sales(outcomes: Iterable[Outcome]) -> int:
    return sum(outcome.sales for outcome in outcomes)


def normalize_probabilities(outcomes: Iterable[Outcome]) -> dict[str, float]:
    outcomes_list = list(outcomes)
    total = total_sales(outcomes_list)
    if total <= 0:
        raise ValueError("Total sales must be positive to compute probabilities.")
    return {outcome.name: outcome.sales / total for outcome in outcomes_list}


def expected_value(outcomes: Iterable[Outcome], ticket_cost: float = 1.0) -> float:
    outcomes_list = list(outcomes)
    probabilities = normalize_probabilities(outcomes_list)
    return sum(probabilities[outcome.name] * outcome.payout for outcome in outcomes_list) - ticket_cost
