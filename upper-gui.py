# Upper.Py version 1.1
# Added Clear button
# by Ken Pryor
# 10/14/2022

from tkinter import *
import pyperclip as pc

root = Tk()
root.title("UpperPy")
root.geometry("500x150")

e=Entry(root, width=150, font=("Arial 18"))
e.pack(pady=20)

def paste():
    clipboard = root.clipboard_get() # Get the copied item from system clipboard
    e.insert('end',clipboard) # Insert the item into the entry widget

def myClick():
    t = e.get()
    u = t.upper()
    myLabel = Label(root, text = u)
    pc.copy(u)
    e.delete(0, END)
    e.insert(0, u)
    myLabel.pack()
    
def myDelete():
    e.delete(0, END)
    


myButton = Button(root, text = 'Paste', height=1, width=10, command=paste)
myButton.pack()      
myButton = Button(root, text = 'Uppify It!', height=1, width=10, command=myClick)
myButton.pack()
myDeleteButton = Button(root, text = 'Clear', height=1, width=10, command=myDelete)
myDeleteButton.pack()
root.mainloop()