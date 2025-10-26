# operator overloading

class op:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        if self.x < other.x:
            return f"{self.x} is lesser than {other.x}"
        else:
            return f"{self.x} is not lesser than {other.x}"

    def __eq__(self, other):
        if self.x == other.x:
            return f"{self.x} is equal to {other.x}"
        else:
            return f"{self.x} is not equal to {other.x}"


obj1 = op(23)
obj2 = op(223)

print(obj1 < obj2)
print(obj1 == obj2)
