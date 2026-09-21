"""Small validation helpers for user input."""


def is_number(value: object) -> bool:
    """Return whether ``value`` can be interpreted as a finite number."""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return False
    return number == number and number not in (float("inf"), float("-inf"))


def is_non_empty(value: object) -> bool:
    """Return whether ``value`` is a non-blank string."""
    return isinstance(value, str) and bool(value.strip())

