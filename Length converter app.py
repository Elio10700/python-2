import tkinter as tk
from tkinter import messagebox

def convert_length():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{inches} inches = {centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("300x200")
root.configure(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Convert Inches to Centimeters", font=("Arial", 14), bg="#f0f0f0")
title_label.pack(pady=10)

# Entry field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_length, font=("Arial", 12), bg="#4CAF50", fg="white")
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=5)

# Run the app
root.mainloop()