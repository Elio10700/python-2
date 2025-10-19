# special function

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


p1 = point(2, 3)
print(p1)
