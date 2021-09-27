'''
Two steps to create anything in Tkinter :
    1. Create the widget
    2. Put that widget onto the screen
'''
# Importing all the things from the tkinter library
from tkinter import *

# This is the root Widget or u may think it as the main Window
root = Tk()

# Creating a Label Widget
# root : means that it is created on root widget
myLable = Label(root,text = "Hello World")

# Showing it onto screen
# pack : It helps the widget get aligned automatically with the size of the window
myLable.pack()

# Creating an Event Loop
# it keeps on running until the cross is clicked to exit the window
root.mainloop()
