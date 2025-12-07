from tkinter import *
from datetime import datetime, date

root = Tk()
root.title("This is my tkinter window")
root.geometry("500x600")

text1 = Text(root, bg = 'aqua')

def greet():
    name = entry1.get()
    now = date.today()
    text1.delete("1.0",'end')
    text1.insert(END, "Hi " + name + " In Today's Date is " + str(now))
   
    entry1.delete(0, 'end')

label = Label(root, text="Enter your name", bg = 'aqua', fg = 'navy')
label.pack(pady=10)
entry1 = Entry(root)
entry1.pack(pady=10)
button1 = Button(root, text="Login", bg = 'navy', fg = 'aqua', command = greet)
button1.pack(pady=10)

text1 = Text(root, bg = 'grey', fg = 'white', width = 50, height = 20)
text1.pack()
