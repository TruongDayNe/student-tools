"""Common unit conversion helpers."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles."""
    return kilometers * 0.621371


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers."""
    return miles / 0.621371

