from tkinter import *

root = Tk()
root.geometry("400x400")

Label(root, text="your first number:").grid(row=0, column=0)
Label(root, text="your second number:").grid(row=1, column=0)
# define the label, step 1
label3 = Label(root)
# set grid, step 2
label3.grid(row=3, column=1)

first_no = IntVar()
second_no = IntVar()

# same goes for here
entry1 = Entry(root, textvariable=first_no).grid(row=0, column=1)
entry2 = Entry(root, textvariable=second_no).grid(row=1, column=1)


def add():
    sumation = first_no.get() + second_no.get()
    label3.config(text="your final number is:" + str(sumation))

# and here
mybutton = Button(root, text=("Calculate!"), command=add).grid(row=2, column=1)

root.mainloop()
