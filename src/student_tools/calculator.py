"""Basic calculator operations."""

from student_tools.validator import is_number


def _validate_numeric(*values: object) -> tuple:
    """Return ``values`` coerced to floats, or raise ``ValueError``.

    Accepting numeric strings (e.g. ``"10"``) means callers must use the
    coerced return value instead of the raw input, otherwise operations
    like ``"10" + 2`` would still raise a raw ``TypeError``.
    """
    validated = []
    for value in values:
        if not is_number(value):
            raise ValueError(f"invalid numeric input: {value!r}")
        validated.append(float(value))
    return tuple(validated)


def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    first, second = _validate_numeric(first, second)
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the difference between two numbers."""
    first, second = _validate_numeric(first, second)
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    first, second = _validate_numeric(first, second)
    return first * second


def divide(first: float, second: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If ``first`` or ``second`` is not a valid number,
            or if ``second`` is zero.
    """
    first, second = _validate_numeric(first, second)
    if second == 0:
        raise ValueError("cannot divide by zero")
    return first / second

