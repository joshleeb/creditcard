from creditcard_validator.luhn import Luhn


class TestLuhn:
  def __init__(self):
    self.luhn = Luhn()

    self.valid_numbers = ["79927398713", "4916123235800351", "36574910273269",
                          "5548175508461272", "6399487244535238", "123455"]
    self.invalid_numbers = ["79927398712", "455644003888259", "12894310578",
                            "66929644595", "1950254148103", "670367965"]

  def test_valid_numbers(self):
    for n in self.valid_numbers:
      yield self.check_valid_numbers, n

  def test_invalid_numbers(self):
    for n in self.invalid_numbers:
      yield self.check_invalid_numbers, n

  def check_valid_numbers(self, n):
    assert self.luhn.is_valid(n) is True

  def check_invalid_numbers(self, n):
    assert self.luhn.is_valid(n) is False
