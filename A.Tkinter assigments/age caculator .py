import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def calculate_age():
    try:
        birth_date = entry.get()
        # Expecting format: YYYY-MM-DD
        birth = datetime.strptime(birth_date, "%Y-%m-%d")
        today = datetime.today()
        
        age_years = today.year - birth.year
        age_months = today.month - birth.month
        age_days = today.day - birth.day

        # Adjust if birthday hasn't happened yet this year
        if age_days < 0:
            age_months -= 1
            age_days += 30  # approximate
        if age_months < 0:
            age_years -= 1
            age_months += 12

        result_label.config(
            text=f"🧬 Age: {age_years} years, {age_months} months, {age_days} days"
        )
    except ValueError:
        messagebox.showerror("Invalid input", "Enter date in YYYY-MM-DD format.")

# Create main window
root = tk.Tk()
root.title("Age Calculator App")
root.geometry("450x250")
root.configure(bg="#0d0d0d")  # Futuristic dark background

# Title
title_label = tk.Label(
    root,
    text="⏳ Age Calculator",
    font=("Orbitron", 18, "bold"),  # Futuristic font
    fg="#00ffcc",  # Neon cyan
    bg="#0d0d0d"
)
title_label.pack(pady=15)

# Input field
entry_label = tk.Label(
    root,
    text="Enter your birthdate (YYYY-MM-DD):",
    font=("Consolas", 12),
    fg="#ffffff",
    bg="#0d0d0d"
)
entry_label.pack()
entry = tk.Entry(root, font=("Consolas", 14), bg="#1a1a1a", fg="#00ffcc", insertbackground="#00ffcc")
entry.pack(pady=8)

# Calculate button
calc_button = tk.Button(
    root,
    text="Calculate ➝",
    command=calculate_age,
    font=("Consolas", 12, "bold"),
    bg="#00ffcc",
    fg="#0d0d0d",
    activebackground="#ff00ff",  # Neon magenta hover
    activeforeground="#ffffff"
)
calc_button.pack(pady=12)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Consolas", 14, "bold"),
    fg="#ff00ff",  # Neon magenta
    bg="#0d0d0d"
)
result_label.pack(pady=10)

# Run the app
root.mainloop()