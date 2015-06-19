# CreditCard

CreditCard is a Python 3 module which can validate, generate and determine the format of credit card numbers using the Luhn algorithm.

## Getting Started

To import the module add the following to your python file:

#### Luhn (Generator and Validator)
    from creditcard import luhn
#### Formatter
    from creditcard.formatter import Formatter
    formatter = Formatter()

### Validator
The validator can be used to validate credit cards and calculate the Luhn check digit for a given number.

#### Validate
To validate a credit card number:

    luhn.is_valid(number)

`number` is a string or integer which is the credit card number.

To calculate the Luhn check digit for a particular number:

    luhn.calculate_check_digit(number)

Again, `number` is a string or integer. For this method, however, it is a partial credit card number. This method will return the check digit, which is the last digit of the card number, as an integer.

### Generator
To generate a valid credit card number:

    luhn.generate(length)

This method will return a valid credit card number as a string.

### Formatter
To check whether a number matches the format of a specified type of credit card use the following methods:

The following card number formats can be detected:

+ visa
+ visa electron
+ mastercard
+ amex (american express)
+ maestro
+ discover

A card number can be checked to be in one of these formats by using the method `formatter.is_format(number)`, where format is the format you are checking.

Each of these method will return `True` or `False` depending on whether the given number
`n` matches the format tested. As with the Validator and Generator, `n` can be
either a string or an integer.

To check if the number matches any of the formats you can use the method `formatter.get_format(number)` which will return a list of all the formats that the number complies with. If the number is determined to not be any of the above formats then an empty list will be returned.
