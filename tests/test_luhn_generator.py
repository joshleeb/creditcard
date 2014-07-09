from creditcard.luhn_validator import LuhnValidator
from creditcard.luhn_generator import LuhnGenerator
from nose.tools import raises
import random


class TestLuhnGenerator:
  def __init__(self):
    self.luhn_val = LuhnValidator()
    self.luhn_gen = LuhnGenerator()

    self.invalid_length_types = [0, 1, -1, "123", 2.1]

  def test_generates_valid_number_of_given_length(self):
    for i in range(3):
      length = random.randint(2, 20)
      yield self.check_generates_valid_number_of_given_length, length

  def test_invalid_length_type_raises_typeerror(self):
    for t in self.invalid_length_types:
      yield self.check_invalid_length_type_raises_typeerror, t

  def check_generates_valid_number_of_given_length(self, length):
    generated_number = self.luhn_gen.generate(length)
    assert self.luhn_val.is_valid(generated_number) is True

  @raises(TypeError)
  def check_invalid_length_type_raises_typeerror(self, length):
    self.luhn_gen.generate(length)

