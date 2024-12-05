from tkinter import *
root = Tk()
show=Label(root, text="|Welcome|")
show.pack()
show1=Label(root,text="_______________________")
show1.pack()


textlab1=Label(root, text="Enter First Number:")
textlab1.pack()
e1 = Entry(root)
e1.pack()

textlab2=Label(root, text="Enter Second Number:")
textlab2.pack()
e2 = Entry(root)
e2.pack()
l = Label(root)
def callback():
    total = sum(int(e.get()) for e in (e1, e2))
    l.config(text="Answer = %s" % total)

b = Button(root, text="add them", command=callback)

for widget in (e1, e2, l, b):
    widget.pack()
b.mainloop()
