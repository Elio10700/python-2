from tkinter import *
from datetime import date

root = Tk()
root.title("Number Pad")
root.geometry("275x320")
root.configure(bg='lightblue')

num = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [',', 0, '.']]

for i in range(4):
    root.rowconfigure(i, weight=0, minsize=70)
    for j in range(3):
        root.columnconfigure(j, weight=2, minsize=80)
        label1 = Label(text=num[i][j], bg='navy', fg='white', bd=2, relief='sunken')
        label1.grid(row=i, column=j)

root.mainloop()