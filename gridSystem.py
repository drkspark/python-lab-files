''' Author : Madhu  Date : 25/09/2021
Grid System


'''
from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello Madhu")
myLabel2 = Label(root, text="I will get into Google")

# Grid are just like Matrix and they are Relative
# The index starts from 0
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=1)

root.mainloop()
