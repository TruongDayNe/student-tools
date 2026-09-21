"""Basic calculator operations."""

from student_tools.validator import is_number


def _validate_numeric(*values: object) -> None:
    """Raise ``ValueError`` if any value is not a valid finite number."""
    for value in values:
        if not is_number(value):
            raise ValueError(f"invalid numeric input: {value!r}")


def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    _validate_numeric(first, second)
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the difference between two numbers."""
    _validate_numeric(first, second)
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    _validate_numeric(first, second)
    return first * second


def divide(first: float, second: float) -> float:
    """Return the quotient of two numbers.

    Raises:
        ValueError: If ``first`` or ``second`` is not a valid number,
            or if ``second`` is zero.
    """
    _validate_numeric(first, second)
    if second == 0:
        raise ValueError("cannot divide by zero")
    return first / second

