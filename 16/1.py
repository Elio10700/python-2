# class convert to uppercase
class Iostring:
    def __init__(self, str1):
        self.str1 = str1

    def up(self):
        print("The uppercase of the string is", self.str1.upper())

s1 = Iostring("python")
s1.up()
