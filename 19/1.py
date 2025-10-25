from abc import ABC, abstractmethod

class abcclass(ABC):
    def printx(self, x):
        print("The value is", x)

    @abstractmethod
    def task(self):
        pass


class inhclass(abcclass):
    def task(self):
        print("I am inside the Inherited class")


obj1 = inhclass()
obj1.task()
obj1.printx(10)
