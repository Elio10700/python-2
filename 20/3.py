# fruit quiz
import random

class fruitquiz:
    def __init__(self):
        self.fruits = {
            "melon": "green",
            "banana": "yellow",
            "apple": "orange",
            "orange": "orange"
        }

    def quiz(self):
        while True:
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of", fruit)
            user = input()
            if user == color:
                print("You are correct")
            else:
                print("You are wrong")

            ch = input("Do you want to continue (y/n): ")
            if ch.lower() == 'n':
                break

obj1 = fruitquiz()
obj1.quiz()