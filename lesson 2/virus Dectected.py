from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Event Handler")
root.geometry("300x400")
root.configure(bg='turquoise')

def msg():
    messagebox.showwarning("alert", "Virus found scan now")

button1 = Button(root, text = "Scan", width = 10, height = 1, bg = "brown", fg = "white", command = msg)
button1.place(x = 120, y = 200)

root.mainloop()
