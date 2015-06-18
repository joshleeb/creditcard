import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from creditcard.luhn import LuhnValidator
from creditcard.luhn import LuhnGenerator


class TestValidator(unittest.TestCase):
    def test_validates_valid_number(self):
        valid = 79927398713
        validator = LuhnValidator()

        self.assertTrue(validator.is_valid(valid))

    def test_invalidates_invalid_number(self):
        invalid = 79927398712
        validator = LuhnValidator()

        self.assertFalse(validator.is_valid(invalid))

    def test_calculates_corerct_check_digit(self):
        unchecked = 12345
        validator = LuhnValidator()

        self.assertEqual(validator.calculate_check_digit(unchecked), 5)

    def test_negative_number_raises_type_error(self):
         validator = LuhnValidator()

         with self.assertRaises(TypeError):
             validator.is_valid(-123)

    def test_decimal_number_raises_type_error(self):
        validator = LuhnValidator()

        with self.assertRaises(TypeError):
            validator.is_valid(123.3)

    def test_string_raises_type_error(self):
        validator = LuhnValidator()

        with self.assertRaises(TypeError):
            validator.is_valid('123.3')


class TestGenerator(unittest.TestCase):
    def test_generates_valid_number_of_specified_length(self):
        generator = LuhnGenerator()
        validator = LuhnValidator()

        number = generator.generate(5)

        self.assertEqual(len(number), 5)
        self.assertTrue(validator.is_valid(number))

    def test_no_length_generates_valid_number_of_random_length(self):
        generator = LuhnGenerator()
        validator = LuhnValidator()

        number = generator.generate()

        self.assertTrue(validator.is_valid(number))

    def test_length_as_float_raises_type_error(self):
        generator = LuhnGenerator()

        with self.assertRaises(TypeError):
            generator.generate(2.1)

    def test_zero_length_raises_type_error(self):
        generator = LuhnGenerator()

        with self.assertRaises(TypeError):
            generator.generate(0)

    def test_length_too_short_raises_type_error(self):
        generator = LuhnGenerator()

        with self.assertRaises(TypeError):
            generator.generate(1)

    def test_negative_length_raises_type_error(self):
        generator = LuhnGenerator()

        with self.assertRaises(TypeError):
            generator.generate(-1)

    def test_length_as_string_raises_type_error(self):
        generator = LuhnGenerator()

        with self.assertRaises(TypeError):
            generator.generate('5')
