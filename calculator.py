'''
Author : Madhu  Date : 27/09/2021
My first ever development project, Hope this teaches me many things.

I will be building a Simple calculator using Python Tkinter library
'''

from tkinter import *
from typing import Match

root = Tk()
# Naming the Main Window
root.title("Simple Calculator")

# Input Box
e = Entry(root,width=35,borderwidth=5)

# We will use grid system to place the things
# columnspan : Tells us how many columns  the box will be occupying
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

# Functions for button click

def button_clear():    # To clear the input TextBox
    e.delete(0, END)

def button_add ():
    global f_num
    global math
    math = "sum"
    f_num = int(e.get())
    e.delete(0, END)

def button_subtract ():
    global f_num
    global math
    math = "difference"
    f_num = int(e.get())
    e.delete(0, END)

def button_multiply ():
    global f_num
    global math
    math = "product"
    f_num = int(e.get())
    e.delete(0, END)

def button_divide ():
    global f_num
    global math
    math = "quotient"
    f_num = int(e.get())
    e.delete(0, END)

def button_equal ():
    s_num = e.get()
    e.delete(0,END)
    
    if math == "sum":
        e.insert(0,f_num+int(s_num))
    if math == "difference":
        e.insert(0,f_num - int(s_num))
    if math == "product":
        e.insert(0,f_num * int(s_num))
    if math == "quotient":
        e.insert(0,f_num // int(s_num))

def buttons_click(num):
    value = e.get()
    e.delete(0, END)
    e.insert(0,str(value)+str(num)) # Just concatinaing the string and displaying it
    return

# Buttons

# Here we used lambda as we can't pass the argumnets directly like button_click(2) : Reason being when the application starts the function will be invoked without clicking the button 
button_1 = Button(root, text='1', padx=40, pady=20,command = lambda : buttons_click(1) )
button_2 = Button(root, text='2', padx=40, pady=20,command = lambda : buttons_click(2) )
button_3 = Button(root, text='3', padx=40, pady=20,command = lambda : buttons_click(3) )
button_4 = Button(root, text='4', padx=40, pady=20,command = lambda : buttons_click(4) )
button_5 = Button(root, text='5', padx=40, pady=20,command = lambda : buttons_click(5) )
button_6 = Button(root, text='6', padx=40, pady=20,command = lambda : buttons_click(6) )
button_7 = Button(root, text='7', padx=40, pady=20,command = lambda : buttons_click(7) )
button_8 = Button(root, text='8', padx=40, pady=20,command = lambda : buttons_click(8) )
button_9 = Button(root, text='9', padx=40, pady=20,command = lambda : buttons_click(9) )
button_0 = Button(root, text='0', padx=40, pady=20,command = lambda : buttons_click(0) )

bt_add = Button(root, text='+',padx=39, pady=20, command=button_add)
bt_subtract = Button(root, text='-',padx=42, pady=20, command=button_subtract)
bt_multiply = Button(root, text='*',padx=41, pady=20, command=button_multiply)
bt_divide = Button(root, text='/',padx=41, pady=20, command=button_divide)
bt_equal= Button(root, text='=',padx=91, pady=20, command=button_equal)
bt_clear = Button(root, text='clear',padx=80, pady=20, command= button_clear)

# Putting Buttons on Screen

button_1.grid(row=3 , column=0)
button_2.grid(row=3 , column=1)
button_3.grid(row=3 , column=2)

button_5.grid(row=2 , column=1)
button_4.grid(row=2 , column=0)
button_6.grid(row=2 , column=2)

button_7.grid(row=1 , column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row=1 , column=2)

button_0.grid(row=4 , column=0)

bt_clear.grid(row=4 ,column=1, columnspan=2)
bt_equal.grid(row=5, column=1, columnspan=2)

bt_add.grid(row= 5, column=0)
bt_subtract.grid(row= 6, column=0)
bt_multiply.grid(row= 6, column=1)
bt_divide.grid(row= 6, column=2)



# Main event Loop
root.mainloop()