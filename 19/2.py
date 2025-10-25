from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass


class human(animal):
    def move(self):
        print("I can walk and run")


class snake(animal):
    def move(self):
        print("I move by crawling")


class fish(animal):
    def move(self):
        print("I move by swimming")
class Animal:
    def move(self):
        print("I move by crawling")

class Fish(Animal):
    def move(self):
        print("I move by swimming")

class Bird(Animal):
    def move(self):
        print("I can fly and move")

class Human(Animal):
    def move(self):
        print("I walk on two legs")

class Snake(Animal):
    def move(self):
        print("I slither on the ground")

# Creating instances and calling their move methods
h1 = Human()
h1.move()

s1 = Snake()
s1.move()

b1 = Bird()
b1.move()