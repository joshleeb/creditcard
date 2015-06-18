def is_visa(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 13 and length <= 16:
        if n[0] == '4':
            return True
    return False


def is_visa_electron(n):
    """Checks if credit card number fits the visa electron format."""
    n, length = str(n), len(str(n))
    form = ['026', '508', '844', '913', '917']

    if length == 16:
        if n[0] == '4':
            if ''.join(n[1:4]) in form or ''.join(n[1:6]) == '17500':
                return True
    return False


def is_mastercard(n):
    """Checks if credit card number fits the mastercard format."""
    n, length = str(n), len(str(n))

    if length >= 16 and length <= 19:
        if ''.join(n[:2]) in strings_between(51, 56):
            return True
    return False


def is_amex(n):
    """Checks if credit card number fits the american express format."""
    n, length = str(n), len(str(n))

    if length == 15:
        if n[0] == '3' and (n[1] == '4' or n[1] == '7'):
            return True
    return False


def is_maestro(n):
    """Checks if credit card number fits the maestro format."""
    n, length = str(n), len(str(n))
    form = ['5018', '5020', '5038', '5893', '6304',
                    '6759', '6761', '6762', '6763']

    if length >= 16 and length <= 19:
        if ''.join(n[:4]) in form:
            return True
    return False


def is_discover(n):
    """Checks if credit card number fits the discover card format."""
    n, length = str(n), len(str(n))

    if length == 16:
        if n[0] == '6':
            if ''.join(n[1:4]) == '011' or n[1] == '5':
                return True
            elif n[1] == '4' and n[2] in strings_between(4, 10):
                return True
            elif ''.join(n[1:6]) in strings_between(22126, 22926):
                return True
    return False


def get_format(n):
    """Gets a list of the formats a credit card number fits."""
    formats = []

    if is_visa(n):
        formats.append('visa')
    if is_visa_electron(n):
        formats.append('visa electron')
    if is_mastercard(n):
        formats.append('mastercard')
    if is_amex(n):
        formats.append('amex')
    if is_maestro(n):
        formats.append('maestro')
    if is_discover(n):
        formats.append('discover')

    return formats


def strings_between(a, b):
    """Generates a list of strings between a and b."""
    return list(map(str, range(a, b)))
