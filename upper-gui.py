# Upper GUI version 1 by Ken Pryor 09/24/2022

from tkinter import *
import pyperclip as pc

root = Tk()
root.title("Upper")

e = Entry(root, width = 100)
e.pack()

def myClick():
    t = e.get()
    u = t.upper()
    myLabel = Label(root, text = u)
    pc.copy(u)
    e.delete(0, END)
    e.insert(0, u)
    myLabel.pack()
    
myButton = Button(root, text = 'Enter your text', command=myClick)
myButton.pack()
root.mainloop()
