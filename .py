from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import Tk, Text, Button, END
def open():
    file = askopenfile(mode='r', filetypes=[('textfiles','*.txt')])
    if file is not None:
        content = file.read()
        text1.delete("1.0", 'end')
        text1.insert(END, content)
        file.close()

def save():
    file = asksaveasfile(mode='w', filetypes=[('textfiles','*.txt')])
    if file is not None:
        mytext1 = text1.get("1.0", "end")
        file.write(mytext1)
        file.close()

window = Tk()
window.title("Text Editor")
window.geometry("500x500")
text1 = Text(window, width=40, height=20, relief='sunken', border=3)
button1 = Button(window, text="open", width=10, command=open)
button2 = Button(window, text="save as", width=10, command=save)

text1.grid(row=1, column=0, padx=10, pady=10)
button1.grid(row=2, column=0, pady=10, padx=10)
button2.grid(row=3, column=1, padx=10, pady=10, rowspan=2)

window.mainloop()
