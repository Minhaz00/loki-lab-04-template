import os
import random

from src.checkout import total


def test_total_simple():
    assert total([("apple", 2, 0.50), ("bread", 1, 2.00)]) == 3.00


def test_total_empty():
    assert total([]) == 0


def test_total_flaky():
    """Deliberately flaky: ~15% failure rate to simulate a real-world flake."""
    flake_rate = float(os.environ.get("FLAKE_RATE", "0.15"))
    if random.random() < flake_rate:
        assert False, "checkout total mismatch (flaky)"
    assert total([("widget", 3, 9.99)]) == 29.97
