from tkinter import *
#from datetime import datetime
#import pytz
import random

root = Tk()
root.title("Restaurant management system")
root.geometry("800x400")
root.configure(bg="beige")

frame1 = Frame(root, width = 500, height = 300, relief = SUNKEN, bg = 'beige')
frame1.pack()

label1 = Label(frame1, font=("arial", 18, 'bold'), 
               text="Restaurant Management System", 
               bg="beige", fg="firebrick")
label1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


drink = StringVar()
pizza = StringVar()
burger = StringVar()
largeburger = StringVar()
fries = StringVar()

labeldrinks = Label(frame1, text = "Drinks", fg = "firebrick", font = ('Times',12,'bold'), bg = "beige")
labeldrinks.grid(row=3,column = 0,padx=10,pady=10)
entrydrink = Entry(frame1,textvariable=drink,justify=RIGHT)
entrydrink.grid(row = 3, column =1,padx=10,pady=10)
entrydrink.insert(END,0)

labelpizza = Label(frame1, text = "Pizza", fg = "firebrick", font = ('Times',12,'bold'),bg = "beige")
labelpizza.grid(row=4,column = 0,padx=10,pady=10)
entrypizza = Entry(frame1,textvariable=pizza,justify=RIGHT)
entrypizza.grid(row = 4, column =1,padx=10,pady=10)
entrypizza.insert(END,0)

labelburger = Label(frame1, text = "Burger", fg = "firebrick", font = ('Times',12,'bold'),bg = "beige")
labelburger.grid(row=5,column = 0,padx=10,pady=10)
entryburger = Entry(frame1,textvariable=burger,justify=RIGHT)
entryburger.grid(row = 5, column =1,padx=10,pady=10)
entryburger.insert(END,0)

labellargeburger = Label(frame1, text = "Large Burger", fg = "firebrick", font = ('Times',12,'bold'),bg = "beige")
labellargeburger.grid(row=6,column = 0,padx=10,pady=10)
entrylargeburger = Entry(frame1,textvariable=largeburger,justify=RIGHT)
entrylargeburger.grid(row = 6, column =1,padx=10,pady=10)
entrylargeburger.insert(END,0)

labelfries = Label(frame1, text = "Fries", fg = "firebrick", font = ('Times',12,'bold'),bg = "beige")
mainloop()