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


if __name__ == "__main__":
    unittest.main()

