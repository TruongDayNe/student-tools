import unittest

from student_tools.validator import is_non_empty, is_number


class ValidatorTests(unittest.TestCase):
    def test_number_validation(self):
        self.assertTrue(is_number("12.5"))
        self.assertTrue(is_number(-3))
        self.assertFalse(is_number("not a number"))
        self.assertFalse(is_number(float("inf")))

    def test_non_empty_validation(self):
        self.assertTrue(is_non_empty("student"))
        self.assertFalse(is_non_empty("   "))
        self.assertFalse(is_non_empty(None))


if __name__ == "__main__":
    unittest.main()

