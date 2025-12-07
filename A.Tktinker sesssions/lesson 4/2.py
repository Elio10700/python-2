from tkinter import *
from tkinter import messagebox
from os import system
root1 = Tk()
root1.title("Denomination Calculator")
root1.geometry("600x600")

#upload = Image.open("app_img.jpg")
#upload = #upload.resize((300, 300))
#img = ImageTk.PhotoImage(upload)

#label1 = Label(root1, image=img)
#label1.place(x=100, y=20)

label2 = Label(root1, text="hey user! welcome to Denomination calculator application")
label2.place(x=20, y=320)

def msg():
    messagebox.showinfo("alert", "do you want to calculate the denomination count ?")
if msg == "ok":
    topwin()
Button1 = Button (root1,text="LET get started!",command=msg,bg='brown',fg='White')
Button1.place(x=180,y=370)

def topwin():
    def calculator():
        global amount
        amount = int(entry1.get())
        note2000 = amount//2000
        note500 = (amount%2000)//500
        note100 = ((amount%2000)%500)//100

        t1.insert(END, str(note2000))
        t2.insert(END, str(note500))
        t3.insert(END, str(note100))

    top = Toplevel()
    top.geometry("400x400")
    Label(top, text = "enter total amount")
    Label.place(x = 100, y = 50)

    entry1 = Entry(top)
    entry1.place(x = 150, y = 100)

    Label(top, text = "here are the numbers of notes for each")
    Label.place(x = 50, y = 150)

    l1 = Label(top, text = "2000")
    l1.place(x = 100, y = 180)
    t1 = Entry(top)
    t1.place(x = 150, y = 180)

    l2 = Label(top, text = "500")
    l2.place(x = 100, y = 210)
    t2 = Entry(top)
    t2.place(x = 150, y = 210)

    l3 = Label(top, text = "100")
    l3.place(x = 100, y = 240)
    t3 = Entry(top)
    t3.place(x = 150, y = 240)

    Button(top, text = "calculate", command = calculator).place(x = 150, y = 280)
    entry1.place(x = 150, y = 100)

    t1.place(x = 150, y = 180)
    l1.place(x = 100, y = 200)

    t2.place(x = 200, y = 230)
    l2.place(x = 200, y = 200)

    t3.place(x = 200, y = 250)
    top.mainloop()
root1.mainloop()

