# CreditCard

CreditCard is a Python 3 module which aids in the validation and generation of credit card numbers using the Luhn algorithm.

## Getting Started

To import the module add the following to your python file:

#### Luhn (Generator and Validator)
    from creditcard.luhn import LuhnValidator
    from creditcard.luhn import LuhnGenerator
#### Formatter
    from creditcard.formatter import Formatter

Then just initialise the classes:

    luhn_validator = LuhnValidator()
    luhn_generator = LuhnGenerator()
    formatter = Formatter()

### Validator
The validator can be used to validate credit cards and calculate the Luhn check
digit for a given number.

#### Validate
To validate a credit card number:

    luhn_validator.is_valid(seq)

`seq` is a string or integer which is the credit card number and must be
entirely digits or a `TypeError` is raised.

To calculate the Luhn check digit for a particular number:

    luhn_validator.calculate_check_digit(seq)

Again, `seq` is a string or integer. For this method, however, it is a partial
credit card number. This method will return the check digit as an integer.

### Generator
To generate a valid credit card number:

    luhn_generator.generate(length)

This method will return a valid credit card number in the form of a string. The
`length` parameter is optional and, if left out, the method will generate a
number of a random length between 2 and 30 inclusive.

### Formatter
To check whether a number matches the format of a specified type of credit
card use the following methods:

    formatter.is_visa(n)
    formatter.is_visa_electron(n)
    formatter.is_mastercard(n)
    formatter.is_amex(n)    # American Express
    formatter.is_maestro(n)
    formatter.is_discover(n)

Each of these method will return `True` or `False` depending on whether the given number
`n` matches the format tested. As with the Validator and Generator, `n` can be
either a string or an integer.

To get the format of a number:

    formatter.get_format(n)

This method will return a list of the formats the number `n` complies with. If
the number doesn't match any formats then the method will return a list with the
single string `"Unknown"`.
