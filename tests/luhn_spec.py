import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from creditcard import luhn


class TestValidation(unittest.TestCase):
    def test_even_digits(self):
        """should get list of digits at even indexes starting at last digit and
        counting from 1."""
        number = 1234567891
        self.assertEqual(luhn.even_digits(number), [9, 7, 5, 3, 1])

    def test_odd_digits(self):
        """should get list of digits at odd indexes starting at last digita and
        counting from 1."""
        number = 1234567891
        self.assertEqual(luhn.odd_digits(number), [1, 8, 6, 4, 2])

    def test_calculates_correct_check_digit(self):
        """should calculate the correct check digit for a number."""
        unchecked = 12345
        self.assertEqual(luhn.get_check_digit(unchecked), 5)

    def test_calculates_correct_check_digit_of_number_as_string(self):
        """should calculate teh correct check digit for a number as a string."""
        unchecked = '12345'
        self.assertEqual(luhn.get_check_digit(unchecked), 5)

    def test_validates_valid_number(self):
        """should validate a valid number."""
        valid = 79927398713
        self.assertTrue(luhn.is_valid(valid))

    def test_validates_valid_number_as_string(self):
        """should validate a valid number as a string."""
        valid = '79927398713'
        self.assertTrue(luhn.is_valid(valid))

    def test_invalidates_invalid_number(self):
        """should invalidate an invalid number."""
        invalid = 79927398712
        self.assertFalse(luhn.is_valid(invalid))

    def test_negative_number_is_invalid(self):
        """should invalidate a negative number."""
        invalid = -123
        self.assertFalse(luhn.is_valid(invalid))

    def test_decimal_number_is_invalid(self):
        """should invalidate a decimal number."""
        invalid = 12.3
        self.assertFalse(luhn.is_valid(invalid))


class TestGenerator(unittest.TestCase):
    def test_generates_valid_number_of_specified_length(self):
        """should generate a valid number of specified length."""
        number = luhn.generate(5)
        self.assertEqual(len(number), 5)
        self.assertTrue(luhn.is_valid(number))

    def test_length_as_float_raises_type_error(self):
        """should raise a TypeError if length is a float."""
        with self.assertRaises(TypeError):
            luhn.generate(2.1)

    def test_zero_length_raises_type_error(self):
        """should raise a TypeError if length is 0."""
        with self.assertRaises(TypeError):
            luhn.generate(0)

    def test_length_too_short_raises_type_error(self):
        """should raise a TypeError if length is too short."""
        with self.assertRaises(TypeError):
            luhn.generate(1)

    def test_negative_length_raises_type_error(self):
        """should raise a TypeError if length is negative."""
        with self.assertRaises(TypeError):
            luhn.generate(-1)
