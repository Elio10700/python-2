from tkinter import *
from datetime import date

root = Tk()
root.title("Number Pad")
root.configure(bg = 'beige')

def login():
    name = entry1.get()
    text1 = Text(root)
    text1.pack()
    text1.delete("1.0", "end")
    text1.insert(END, "Hey " + name + ", You have successfully logged in")

frame1 = Frame(root, bg = "darkgrey", height = 150, width = 300, bd = 3)
frame1.pack()

label1 = Label(frame1, text = "name", bg = "darkgrey", fg = "white")
label1.pack(pady=5)

entry1 = Entry(frame1)
entry1.pack(pady=5)

label2 = Label(frame1, text = "Password", bg = "darkgrey", fg = "white")
label2.pack(pady=5)

entry2 = Entry(frame1, show = "*")
entry2.pack(pady=5)
text1 = Text(root,bg = 'beige',bd =1 , width = 200,height = 500, relief='sunken')
root.mainloop()
