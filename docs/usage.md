# Student Tools Usage

## Calculator

```python
from student_tools.calculator import add, divide, multiply, subtract

add(2, 3)       # 5
subtract(5, 3)  # 2
multiply(2, 3)   # 6
divide(6, 3)     # 2.0
```

`divide` raises `ValueError` với thông báo `cannot divide by zero` khi mẫu số bằng 0.

## Converter

```python
from student_tools.converter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    kilometers_to_miles,
    miles_to_kilometers,
)

celsius_to_fahrenheit(0)    # 32.0
celsius_to_fahrenheit(-40)  # -40.0
fahrenheit_to_celsius(32)   # 0.0
celsius_to_kelvin(0)        # 273.15
kelvin_to_celsius(273.15)   # 0.0
fahrenheit_to_kelvin(32)    # 273.15
kilometers_to_miles(10)
miles_to_kilometers(10)
```

## Validator

```python
from student_tools.validator import is_non_empty, is_number

is_number("12.5")       # True
is_number("not number") # False
is_non_empty("student") # True
is_non_empty("   ")     # False
```

## Chạy test

Chạy từ thư mục gốc của repository:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

