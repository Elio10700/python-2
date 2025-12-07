from tkinter import *

root = Tk()
root.title("Mainwindow")
root.geometry("500x500")
root.configure(bg = 'pink')

def top():
    top1 = Toplevel()
    top1.title("Top window")
    top1.geometry("200x200")
    top1.configure(bg="Goldenrod")
    label2 = Label(top1, text='This is the toplevelwindow window', bg='violet')
    label2.pack(pady=20)
    top1.mainloop()

label1 = Label(root, text='This is the main window', bg='pink')
label1.pack(pady=20)
button1 = Button(root, text='click me', command=top)
button1.pack(pady=20)

root.mainloop()