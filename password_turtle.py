import turtle
import random
import string

class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length

    def generate(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(self.length))

class PasswordGuesser:
    def __init__(self, password, screen, writer):
        self.password = password
        self.screen = screen
        self.writer = writer
        self.result_y = -50

    def display_password(self):
        self.writer.goto(0, 100)
        self.writer.write(f"Generated Password:\n{self.password}", align="center", font=("Arial", 16, "bold"))

    def ask_guess(self):
        guess = self.screen.textinput("Password Guesser", "Enter the password:")
        self.writer.goto(0, self.result_y)
        self.writer.clear()  # Clear previous result
        self.display_password()  # Redisplay password after clear
        if guess == self.password:
            self.writer.goto(0, self.result_y)
            self.writer.write("Correct! You guessed the password.", align="center", font=("Arial", 16, "bold"))
        else:
            self.writer.goto(0, self.result_y)
            self.writer.write("Incorrect! Try again.", align="center", font=("Arial", 16, "bold"))
            self.screen.ontimer(self.ask_guess, 1000)

# Setup Turtle screen
screen = turtle.Screen()
screen.title("Password Generator & Guesser")
screen.setup(width=600, height=400)

# Turtle for writing text
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Use classes for password generation and guessing
generator = PasswordGenerator(length=8)
password = generator.generate()

guesser = PasswordGuesser(password, screen, writer)
guesser.display_password()
screen.ontimer(guesser.ask_guess, 1000)

turtle.done()
