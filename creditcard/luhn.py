import random


def get_check_digit(unchecked):
    """returns the check digit of the card number."""
    digits = digits_of(unchecked)
    checksum = sum(even_digits(unchecked)) + sum([
        sum(digits_of(2 * d)) for d in odd_digits(unchecked)])
    return 9 * checksum % 10


def is_valid(number):
    """determines whether the card number is valid."""
    n = str(number)
    if not n.isdigit():
        return False
    return int(n[-1]) == get_check_digit(n[:-1])


def digits_of(number):
    """gets the digits of a number in a list."""
    return [int(d) for d in str(number)]


def even_digits(number):
    """gets a list of digits at even indexes of the number starting at the last
    digit and counting from 1."""
    return list(map(int, str(number)[-2::-2]))


def odd_digits(number):
    """gets a list of digits at odd indexes of the number starting at the last
    digit and counting from 1."""
    return list(map(int, str(number)[-1::-2]))


def generate(length):
    """Generates random and valid card number which is returned as a string."""
    if not isinstance(length, int) or length < 2:
        raise TypeError('length must be a positive integer greater than 1.')

    # first digit cannot be 0
    digits = [random.randint(1, 9)]

    for i in range(length-2):
        digits.append(random.randint(0, 9))
    digits.append(get_check_digit(''.join(map(str, digits))))

    return ''.join(map(str, digits))
