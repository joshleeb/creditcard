from creditcard.luhn import LuhnValidator
from creditcard.luhn import LuhnGenerator
import random
import pytest


class TestLuhnGenerator:

    invalid_types = [0, 1, -1, '123', 2.1]


    def setup_class(self):
        self.val = LuhnValidator()
        self.gen = LuhnGenerator()

    def test_generated_valid_number_of_given_length(self):
        length = random.randint(2, 30)
        seq = self.gen.generate(length)
        assert len(seq) == length

    def test_no_length_generates_number_of_random_length(self):
        seq = self.gen.generate()
        assert len(seq) >= 2 and len(seq) <= 30

    def test_invalid_length_type_raises_type_error(self, invalid_len_types):
        with pytest.raises(TypeError):
            self.gen.generate(invalid_len_types)

    @pytest.fixture(params=invalid_types)
    def invalid_len_types(request):
        return request.invalid_types
