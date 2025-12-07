import tkinter as tk
import random

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Display user and computer choices
    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)


# --- Tkinter Window Setup ---
root = tk.Tk()
root.title("Rock Paper Scissors App")
root.geometry("400x300")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18))
title_label.pack(pady=10)

user_label = tk.Label(root, text="", font=("Arial", 12))
user_label.pack()

comp_label = tk.Label(root, text="", font=("Arial", 12))
comp_label.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
result_label.pack(pady=10)

# --- Buttons ---
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=10)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=10)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=10)

root.mainloop()
