class Formatter:
    """
    Determines the format, or possible formats, of a given credit card number.
    """

    def __init__(self):
        pass

    def is_visa(self, n):
        """Checks if credit card number fits the visa format."""
        n, length = str(n), len(str(n))

        if length >= 13 and length <= 16:
            if n[0] == "4":
                return True
        return False

    def is_visa_electron(self, n):
        """Checks if credit card number fits the visa electron format."""
        n, length = str(n), len(str(n))
        form = ["026", "508", "844", "913", "917"]

        if length == 16:
            if n[0] == "4":
                if ''.join(n[1:4]) in form or ''.join(n[1:6]) == "17500":
                    return True
        return False

    def is_mastercard(self, n):
        """Checks if credit card number fits the mastercard format."""
        n, length = str(n), len(str(n))

        if length >= 16 and length <= 19:
            if ''.join(n[:2]) in self.strings_between(51, 56):
                return True
        return False

    def is_amex(self, n):
        """Checks if credit card number fits the american express format."""
        n, length = str(n), len(str(n))

        if length == 15:
            if n[0] == "3" and (n[1] == "4" or n[1] == "7"):
                return True
        return False

    def is_maestro(self, n):
        """Checks if credit card number fits the maestro format."""
        n, length = str(n), len(str(n))
        form = ["5018", "5020", "5038", "5893", "6304",
                        "6759", "6761", "6762", "6763"]

        if length >= 16 and length <= 19:
            if ''.join(n[:4]) in form:
                return True
        return False

    def is_discover(self, n):
        """Checks if credit card number fits the discover card format."""
        n, length = str(n), len(str(n))

        if length == 16:
            if n[0] == "6":
                if ''.join(n[1:4]) == "011" or n[1] == "5":
                    return True
                elif n[1] == "4" and n[2] in self.strings_between(4, 10):
                    return True
                elif ''.join(n[1:6]) in self.strings_between(22126, 22926):
                    return True
        return False

    def get_format(self, n):
        """Gets a list of the formats a credit card number fits."""
        formats = []

        if self.is_visa(n):
            formats.append("VISA")
        if self.is_visa_electron(n):
            formats.append("VISA ELECTRON")
        if self.is_mastercard(n):
            formats.append("MASTERCARD")
        if self.is_amex(n):
            formats.append("AMEX")
        if self.is_maestro(n):
            formats.append("MAESTRO")
        if self.is_discover(n):
            formats.append("DISCOVER")

        if len(formats) == 0:
            return ["Unknown"]
        return formats

    def strings_between(self, a, b):
        """Generates a list of strings between a and b."""
        return list(map(str, range(a, b)))
