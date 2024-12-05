# Import Module
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to GeekForGeeks")
# Set geometry(widthxheight)
root.geometry('350x200')

# adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when
# button is clicked
def clicked():

    res = "You wrote: " + txt.get()
    lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# Execute Tkinter
root.mainloop()
