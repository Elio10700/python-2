# computer price

class computer:
    def __init__(self):
        self.__maxprice = 900

    def pprice(self):
        print("The max price of the computer is", self.__maxprice)

    def setprice(self, p):
        self.__maxprice = p


c1 = computer()
c1.pprice()

c1.__maxprice = 1000
c1.pprice()

c1.setprice(1400)
c1.pprice()
