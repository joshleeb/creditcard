import random


class LuhnValidator:
    def __init__(self):
        pass

    def calculate_check_digit(self, seq):
        digits, checksum = self.digits_of(seq), 0
        even_digits, odd_digits = self.even_loc(digits), self.odd_loc(digits)

        checksum += sum(even_digits)
        checksum += sum([sum(self.digits_of(2*d)) for d in odd_digits])
        check_digit = 9 * checksum % 10

        return check_digit

    def is_valid(self, seq):
        seq = str(seq)
        if not seq.isdigit():
            raise TypeError("Sequence mus be a string or positive integer.")
        return int(seq[-1]) == self.calculate_check_digit(seq[:-1])

    def digits_of(self, n):
        return [int(d) for d in str(n)]

    def even_loc(self, seq):
        """ Returns a list of the element of even indexes within seq """
        return seq[-2::-2]

    def odd_loc(self, seq):
        """ Returns a list of the element of odd indexes within seq """
        return seq[-1::-2]


class LuhnGenerator:
    def __init__(self):
        self.luhn_validator = LuhnValidator()

    def generate(self, length=None):
        number_list = []

        if length is None:
            length = random.randint(2, 30)
        if not isinstance(length, int) or length < 2:
            raise TypeError("Length must be a positive integer > 1.")

        for i in range(length-1):
            number_list.append(str(random.randint(0, 9)))
        number = ''.join(number_list)
        number_list.append(self.luhn_validator.calculate_check_digit(number))

        return ''.join(list(map(str, number_list)))
