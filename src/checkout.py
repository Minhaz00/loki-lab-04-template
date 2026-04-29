def total(items: list[tuple[str, int, float]]) -> float:
    """Sum quantity * unit_price across (name, quantity, unit_price) tuples."""
    return round(sum(qty * price for _, qty, price in items), 2)
