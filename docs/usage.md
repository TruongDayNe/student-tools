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

## Converter Usage

### Temperature Conversion

Convert Celsius to Fahrenheit:

```python
from student_tools.converter import celsius_to_fahrenheit

result = celsius_to_fahrenheit(0)
print(result)
```

Expected result:

```text
32.0
```

Convert Fahrenheit to Celsius:

```python
from student_tools.converter import fahrenheit_to_celsius

result = fahrenheit_to_celsius(32)
print(result)
```

Expected result:

```text
0.0
```

### Distance Conversion

```python
from student_tools.converter import kilometers_to_miles, miles_to_kilometers

kilometers_to_miles(10)
miles_to_kilometers(10)
```

### Length Conversion

```python
from student_tools.converter import kilometers_to_meters, meters_to_kilometers

meters_to_kilometers(1000)  # 1.0
kilometers_to_meters(1)     # 1000
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
