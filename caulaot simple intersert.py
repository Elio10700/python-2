import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")  # "Dark", "Light", or "System"
ctk.set_default_color_theme("blue")

def calculate():
    try:
        p = float(entry_principal.get())
        r = float(entry_rate.get())
        t = float(entry_time.get())
        si = p * r * t / 100.0
        total = p + si
        result_var.set(f"Simple Interest: {si:.2f}    Total Amount: {total:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values for Principal, Rate, and Time.")

def clear():
    entry_principal.delete(0, ctk.END)
    entry_rate.delete(0, ctk.END)
    entry_time.delete(0, ctk.END)
    result_var.set("")

root = ctk.CTk()
root.title("Simple Interest Calculator")
root.geometry("480x260")
root.resizable(False, False)

font_lbl = ("Arial", 12)
font_entry = ("Arial", 12)

lbl_principal = ctk.CTkLabel(root, text="Principal (P):", font=font_lbl)
lbl_principal.grid(row=0, column=0, padx=12, pady=12, sticky="e")
entry_principal = ctk.CTkEntry(root, font=font_entry)
entry_principal.grid(row=0, column=1, padx=12, pady=12)

lbl_rate = ctk.CTkLabel(root, text="Rate (%) (R):", font=font_lbl)
lbl_rate.grid(row=1, column=0, padx=12, pady=12, sticky="e")
entry_rate = ctk.CTkEntry(root, font=font_entry)
entry_rate.grid(row=1, column=1, padx=12, pady=12)

lbl_time = ctk.CTkLabel(root, text="Time (years) (T):", font=font_lbl)
lbl_time.grid(row=2, column=0, padx=12, pady=12, sticky="e")
entry_time = ctk.CTkEntry(root, font=font_entry)
entry_time.grid(row=2, column=1, padx=12, pady=12)

btn_calc = ctk.CTkButton(root, text="Calculate", width=120, command=calculate)
btn_calc.grid(row=3, column=0, padx=12, pady=12)

btn_clear = ctk.CTkButton(root, text="Clear", width=120, command=clear)
btn_clear.grid(row=3, column=1, padx=12, pady=12)

result_var = ctk.StringVar()
lbl_result = ctk.CTkLabel(root, textvariable=result_var, font=("Arial", 11), text_color="blue")
lbl_result.grid(row=4, column=0, columnspan=2, padx=12, pady=12)

root.mainloop()



