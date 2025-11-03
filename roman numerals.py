class IntegerToRoman:
    """
    A simple class to convert integers to Roman numerals (1..3999).
    Usage:
        r = IntegerToRoman(1994)
        print(r.to_roman())  # "MCMXCIV"
    """

    _MAP = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value <= 0 or value > 3999:
            raise ValueError("value must be between 1 and 3999 inclusive")
        self.value = value

    def to_roman(self) -> str:
        n = self.value
        parts = []
        for val, sym in self._MAP:
            if n == 0:
                break
            count, n = divmod(n, val)
            if count:
                parts.append(sym * count)
        return "".join(parts)

    def __str__(self) -> str:
        return self.to_roman()

    @classmethod
    def from_int(cls, value: int) -> "IntegerToRoman":
        return cls(value)