from cc_val.luhn import Luhn
from nose.tools import raises


class TestLuhn:
  def __init__(self):
    self.luhn = Luhn()

    self.valid_numbers = [79927398713, 4916123235800351, 36574910273269,
                          5548175508461272, 6399487244535238, 123455]
    self.invalid_numbers = [79927398712, 455644003888259, 12894310578,
                            66929644595, 1950254148103, 670367965]
    self.invalid_types = [12345.5, "12345.5", "hello", -12345]

  def test_valid_numbers(self):
    for n in self.valid_numbers:
      yield self.check_valid_numbers, n

  def test_invalid_numbers(self):
    for n in self.invalid_numbers:
      yield self.check_invalid_numbers, n

  def test_number_input_as_string(self):
    assert self.luhn.is_valid("123455") is True

  def test_number_input_as_int(self):
    assert self.luhn.is_valid(123455) is True

  def test_invalid_input_types_raises_typeerror(self):
    for n in self.invalid_types:
      yield self.check_invalid_input_types, n

  def check_valid_numbers(self, n):
    assert self.luhn.is_valid(n) is True

  def check_invalid_numbers(self, n):
    assert self.luhn.is_valid(n) is False

  @raises(TypeError)
  def check_invalid_input_types(self, n):
    self.luhn.is_valid(n)
