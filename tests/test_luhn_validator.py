from creditcard.luhn import LuhnValidator
import pytest


class TestLuhnValidator:

    valid = [79927398713, 4916123235800351, 36574910273269,
             5548175508461272, 6399487244535238, 123455]
    invalid = [79927398712, 455644003888259, 12894310578,
               66929644595, 1950254148103, 670367965]
    check = [{"n": 12345, "digit": 5},
             {"n": 492939528948453, "digit": 1},
             {"n": 670984227749358, "digit": 7}]
    invalid_types = [12345.5, "12345.5", "hello", -12345]


    def setup_class(self):
        self.val = LuhnValidator()

    @pytest.mark.parametrize('valid', valid)
    def test_valid_numbers(self, valid):
        assert self.val.is_valid(valid) is True

    @pytest.mark.parametrize('invalid', invalid)
    def test_invalid_numbers(self, invalid):
        assert self.val.is_valid(invalid) is False

    @pytest.mark.parametrize('check', check)
    def test_calculates_correct_check_digit(self, check):
        assert self.val.calculate_check_digit(check['n']) == check['digit']

    @pytest.mark.parametrize('invalid_types', invalid_types)
    def test_invalid_input_type_raises_type_error(self, invalid_types):
        with pytest.raises(TypeError):
            self.val.is_valid(invalid_types)
