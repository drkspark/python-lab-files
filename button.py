from tkinter import *

root = Tk()

# myButton = Button(root, text='Click Me')
# When state = DISABLED, the button is disabled Haha idiot

def myClick():
    myLabel = Label(root, text="Look I made button do something!!")
    myLabel.pack()

# command takes the function which have to do the thing
# Don't use command = myClick() : Reason, if we give the () the program will automatically call the funnction when the program starts 
# Use fg = "color" to change the Text Color
# Use bg = "color" to change the Button Color
myButton = Button(root, text='Click Me',command = myClick,fg = 'Green',bg = 'Red')

# myButton = Button(root, text="Click Me",padx=50,pady = 50 )
# We can change the size with padx and pady
myButton.pack()



root.mainloop()