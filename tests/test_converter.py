import unittest

from student_tools.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_meters,
    kilometers_to_miles,
    meters_to_kilometers,
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

    def test_length_conversion(self):
        self.assertEqual(meters_to_kilometers(1000), 1)
        self.assertEqual(meters_to_kilometers(500), 0.5)
        self.assertEqual(kilometers_to_meters(1), 1000)
        self.assertEqual(kilometers_to_meters(0.5), 500)

    def test_length_conversion_round_trip(self):
        kilometers = meters_to_kilometers(2500)
        self.assertAlmostEqual(kilometers_to_meters(kilometers), 2500)

    def test_length_conversion_zero(self):
        self.assertEqual(meters_to_kilometers(0), 0)
        self.assertEqual(kilometers_to_meters(0), 0)

    def test_length_conversion_negative(self):
        self.assertEqual(meters_to_kilometers(-1000), -1)
        self.assertEqual(kilometers_to_meters(-1), -1000)


if __name__ == "__main__":
    unittest.main()

