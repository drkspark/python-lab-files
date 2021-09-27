'''
Author : Madhu  Date : 26/09/2021
Taking input using Entry
'''
from tkinter import *

root = Tk()

# We can use - width : To change size, bg : back grround color, fg : foreground Color 
# borderwidth : To change border
e = Entry(root, width = 30)
e.pack()
# insert() : Gives the default value inside the input box, Huh but we have to delete it before we can enter our data 
e.insert(0,"Enter your Name")


def myClick():
    # We can use normal Python code
    var = "Hello " + e.get()
    myLabel = Label(root, text = var)
    # myLabel = Label(root, text = "Hello!! " + e.get())
    myLabel.pack()

myButton = Button(root, text="Enter your Name",command=myClick)
myButton.pack()



root.mainloop()