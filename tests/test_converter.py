import unittest

from student_tools.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
)


class ConverterTests(unittest.TestCase):
    def test_temperature_conversion(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
        self.assertEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_distance_conversion_round_trip(self):
        miles = kilometers_to_miles(10)
        self.assertAlmostEqual(miles_to_kilometers(miles), 10)


if __name__ == "__main__":
    unittest.main()

