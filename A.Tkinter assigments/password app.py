import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password.")
    elif length < 4:
        result_label.config(text="Password Strength: Very Weak")
    elif length < 8:
        result_label.config(text="Password Strength: Weak")
    elif length < 12:
        result_label.config(text="Password Strength: Medium")
    else:
        result_label.config(text="Password Strength: Strong")


# --- GUI Window ---
root = tk.Tk()
root.title("Password Strength Checker App")
root.geometry("400x250")

title_label = tk.Label(root, text="Password Strength Checker", font=("Arial", 16))
title_label.pack(pady=10)

tk.Label(root, text="Enter Password:").pack()

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=check_strength)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
