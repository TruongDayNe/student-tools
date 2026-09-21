import unittest

from student_tools.calculator import add, divide, multiply, subtract


class CalculatorTests(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(divide(6, 3), 2)

    def test_divide_by_zero_raises_meaningful_error(self):
        with self.assertRaisesRegex(ValueError, "cannot divide by zero"):
            divide(10, 0)

    def test_invalid_numeric_input_raises_meaningful_error(self):
        with self.assertRaisesRegex(ValueError, "invalid numeric input"):
            add("abc", 2)
        with self.assertRaisesRegex(ValueError, "invalid numeric input"):
            subtract(1, None)
        with self.assertRaisesRegex(ValueError, "invalid numeric input"):
            multiply(float("inf"), 2)
        with self.assertRaisesRegex(ValueError, "invalid numeric input"):
            divide("10", "x")

    def test_numeric_strings_are_coerced_before_operation(self):
        self.assertEqual(add("10", 2), 12)
        self.assertEqual(subtract("5", "3"), 2)
        self.assertEqual(multiply("2", 3), 6)
        self.assertEqual(divide("10", "2"), 5)


if __name__ == "__main__":
    unittest.main()

