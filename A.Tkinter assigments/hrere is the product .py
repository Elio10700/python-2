import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")


root = tk.Tk()
root.title("Product Calculator")


tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=5)

calc_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Product: ")
result_label.grid(row=3, column=0, columnspan=2, pady=5)


root.mainloop()