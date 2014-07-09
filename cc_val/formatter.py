class Formatter:
  def __init__(self):
    pass

  def is_visa(self, n):
    n, length = str(n), len(str(n))
    if length >= 13 and length <= 16:
      if n[0] == "4":
        return True
    return False

  def is_visa_electron(self, n):
    n, length = str(n), len(str(n))
    form = ["026", "508", "844", "913", "917"]
    if length == 16:
      if n[0] == "4":
        if ''.join(n[1:4]) in form or ''.join(n[1:6]) == "17500":
          return True
    return False

  def is_mastercard(self, n):
    n, length = str(n), len(str(n))
    if length >= 16 and length <= 19:
      if ''.join(n[:2]) in self.range_list(51, 56):
        return True
    return False

  def is_amex(self, n):
    n, length = str(n), len(str(n))
    if length == 15:
      if n[0] == "3" and (n[1] == "4" or n[1] == "7"):
        return True
    return False

  def is_maestro(self, n):
    n, length = str(n), len(str(n))
    form = ["5018", "5020", "5038", "5893", "6304",
            "6759", "6761", "6762", "6763"]
    if length >= 16 and length <= 19:
      if ''.join(n[:4]) in form:
        return True
    return False

  def is_discover(self, n):
    n, length = str(n), len(str(n))
    if length == 16:
      if n[0] == "6":
        if ''.join(n[1:4]) == "011" or n[1] == "5":
          return True
        elif n[1] == "4" and n[2] in self.range_list(4, 10):
          return True
        elif ''.join(n[1:6]) in self.range_list(22126, 22926):
          return True
    return False

  def range_list(self, a, b):
    return list(map(str, list(range(a, b))))
