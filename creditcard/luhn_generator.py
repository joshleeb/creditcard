from .luhn_validator import LuhnValidator
import random

class LuhnGenerator:
  def __init__(self):
    self.luhn_validator = LuhnValidator()

  def generate(self, length):
    number_list = []

    if not isinstance(length, int) or length < 2:
      raise TypeError("Length must be a positive integer > 1.")

    for i in range(length-1):
      number_list.append(str(random.randint(0, 9)))

    number = ''.join(number_list)
    number_list.append(self.luhn_validator.calculate_check_digit(number))

    return ''.join(list(map(str, number_list)))
