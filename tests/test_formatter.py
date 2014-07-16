from creditcard.formatter import Formatter
from nose.tools import raises


class TestFormatter:
  def __init__(self):
    self.formatter = Formatter()

    self.visa_numbers = ["4916624087607943", 4024007183310266,
                         4024007122988156, 4024007156941956]
    self.visa_electron_numbers = ["4508077077058854", 4913114684445718,
                                  4175004688713760, 4508339116627051]
    self.mastercard_numbers = ["5307552352810393", 5359901154463751,
                               5409219472999830, 5248186141538791]
    self.amex_numbers = ["349249900257257", 349846877491031,
                         374619657687666, 345197987944152]
    self.maestro_numbers = ["6761105416550351", 5038342256546483,
                            6304236404755563, 5893380289980802]
    self.discover_numbers = ["6011914284657042", 6221284610850936,
                             6011359876556543, 6511610084735901]

  def test_visa_numbers(self):
    for n in self.visa_numbers:
      yield self.check_visa_numbers, n

  def test_visa_electron_numbers(self):
    for n in self.visa_electron_numbers:
      yield self.check_visa_electron_numbers, n

  def test_mastercard_numbers(self):
    for n in self.mastercard_numbers:
      yield self.check_mastercard_numbers, n

  def test_amex_numbers(self):
    for n in self.amex_numbers:
      yield self.check_amex_numbers, n

  def test_maestro_numbers(self):
    for n in self.maestro_numbers:
      yield self.check_maestro_numbers, n

  def tet_discover_numbers(self):
    for n in self.discover_numbers:
      yield self.check_discover_numbers, n

  def test_get_formats_if_unknown_format(self):
    unknown_format = 1234567890
    assert self.formatter.get_format(unknown_format) == ["Unknown"]

  def test_get_formats_if_dual_format(self):
    dual_format = 4508077077058854
    assert self.formatter.get_format(dual_format) == ["VISA", "VISA ELECTRON"]

  def check_visa_numbers(self, n):
    assert self.formatter.is_visa(n) is True

  def check_visa_electron_numbers(self, n):
    assert self.formatter.is_visa_electron(n) is True

  def check_mastercard_numbers(self, n):
    assert self.formatter.is_mastercard(n) is True

  def check_amex_numbers(self, n):
    assert self.formatter.is_amex(n) is True

  def check_maestro_numbers(self, n):
    assert self.formatter.is_maestro(n) is True

  def check_discover_numbers(self, n):
    assert self.formatter.is_discover(n) is True
