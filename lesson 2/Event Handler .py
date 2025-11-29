from tkinter import *

root = Tk()
root.title("Event Handler")
root.geometry("200x200")

def handle_keypress(event):
    print(event.char)

root.bind("<Key>", handle_keypress)

button1 = Button(text="Click me!")
button1.pack()

def handle_click(event):
    print("Button clicked")

button1.bind("<Button-1>", handle_click)
root.mainloop()
