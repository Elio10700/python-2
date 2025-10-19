# Private variable

class private:
    __private_var = 20

    def __private_meth(self):
        print("I am a private method")

    def print_value(self):
        print("The value of the private variable is", self.__private_var)


obj1 = private()
obj1.print_value()
print(obj1.__private_var)
    