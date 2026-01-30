import pytest

from n3.ev import Outcome, expected_value, normalize_probabilities, total_sales


def test_total_sales() -> None:
    outcomes = [Outcome("777", 10, 5.0), Outcome("700", 5, 2.0)]
    assert total_sales(outcomes) == 15


def test_normalize_probabilities() -> None:
    outcomes = [Outcome("777", 10, 5.0), Outcome("700", 5, 2.0)]
    probabilities = normalize_probabilities(outcomes)
    assert probabilities["777"] == pytest.approx(2 / 3)
    assert probabilities["700"] == pytest.approx(1 / 3)


def test_expected_value() -> None:
    outcomes = [Outcome("777", 10, 5.0), Outcome("700", 5, 2.0)]
    ev = expected_value(outcomes, ticket_cost=1.0)
    expected = (2 / 3) * 5.0 + (1 / 3) * 2.0 - 1.0
    assert ev == pytest.approx(expected)
