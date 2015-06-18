# TODO: add tests for error handling

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from creditcard.formatter import Formatter


class TestFormatter(unittest.TestCase):
    def test_should_identify_visa_number(self):
        visa_number = 4024007183310266
        formatter = Formatter()

        self.assertTrue(formatter.is_visa(visa_number))

    def test_should_identify_visa_number_string(self):
        visa_string = "4024007183310266"
        formatter = Formatter()

        self.assertTrue(formatter.is_visa(visa_string))

    def test_should_identify_visa_electron_number(self):
        visa_electron_number = 4175004688713760
        formatter = Formatter()

        self.assertTrue(formatter.is_visa_electron(visa_electron_number))

    def test_should_identify_visa_electron_number_string(self):
        visa_electron_string = "4175004688713760"
        formatter = Formatter()

        self.assertTrue(formatter.is_visa_electron(visa_electron_string))

    def test_should_identify_mastercard_number(self):
        mastercard_number = 5409219472999830
        formatter = Formatter()

        self.assertTrue(formatter.is_mastercard(mastercard_number))

    def test_should_identify_mastercard_number_string(self):
        mastercard_string = "5409219472999830"
        formatter = Formatter()

        self.assertTrue(formatter.is_mastercard(mastercard_string))

    def test_should_identify_amex_number(self):
        amex_number = 374619657687666
        formatter = Formatter()

        self.assertTrue(formatter.is_amex(amex_number))

    def test_should_identify_amex_number_string(self):
        amex_string = "374619657687666"
        formatter = Formatter()

        self.assertTrue(formatter.is_amex(amex_string))

    def test_should_identify_maestro_number(self):
        maestro_number = 6304236404755563
        formatter = Formatter()

        self.assertTrue(formatter.is_maestro(maestro_number))

    def test_should_identify_maestro_number_string(self):
        maestro_string = "6304236404755563"
        formatter = Formatter()

        self.assertTrue(formatter.is_maestro(maestro_string))

    def test_should_identify_discover_number(self):
        discover_number = 6011359876556543
        formatter = Formatter()

        self.assertTrue(formatter.is_discover(discover_number))

    def test_should_identify_discover_number_string(self):
        discover_string = "6011359876556543"
        formatter = Formatter()

        self.assertTrue(formatter.is_discover(discover_string))

    def test_should_return_none_for_unknown_formats(self):
        unknown = 1234567890
        formatter = Formatter()

        self.assertEqual(formatter.get_format(unknown), ['Unknown'])

    def test_should_get_single_format_of_number(self):
        number = 5409219472999830
        formatter = Formatter()

        self.assertEqual(formatter.get_format(number), ['MASTERCARD'])

    def test_should_get_both_formats_of_number(self):
        number = 4508077077058854
        formatter = Formatter()

        self.assertEqual(formatter.get_format(number), ['VISA', 'VISA ELECTRON'])
