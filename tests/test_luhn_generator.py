from creditcard.luhn import LuhnValidator
from creditcard.luhn import LuhnGenerator
import random
import pytest


class TestLuhnGenerator:
    """
    Tests the LuhnGenerator methods.
    """

    invalid_types = [0, 1, -1, '123', 2.1]

    def setup_class(self):
        self.val = LuhnValidator()
        self.gen = LuhnGenerator()

    def test_generated_valid_number_of_given_length(self):
        """Tests a card number should be generated of a specified length."""
        length = random.randint(2, 30)
        seq = self.gen.generate(length)
        assert len(seq) == length

    def test_no_length_generates_number_of_random_length(self):
        """When no length is given a card number of random length is
        generated."""
        seq = self.gen.generate()
        assert len(seq) >= 2 and len(seq) <= 30

    @pytest.mark.parametrize('invalid_types', invalid_types)
    def test_invalid_length_type_raises_type_error(self, invalid_types):
        """Tests invalid length input should raise a TypeError."""
        with pytest.raises(TypeError):
            self.gen.generate(invalid_types)
