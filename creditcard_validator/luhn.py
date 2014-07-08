class Luhn:
  def __init__(self):
    pass

  def digits_of(self, n):
    return [int(d) for d in str(n)]

  def calculate_check_digit(self, seq):
    digits, checksum = self.digits_of(seq), 0
    odd_indexes, even_indexes = digits[-1::-2], digits[-2::-2]

    checksum += sum(even_indexes)
    checksum += sum([sum(self.digits_of(2*d)) for d in odd_indexes])
    check_digit = 9 * checksum % 10

    return check_digit

  def is_valid(self, seq):
    return int(seq[-1]) == self.calculate_check_digit(seq[:-1])
