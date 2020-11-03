"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()

f1 = Frame()
f2 = Frame()
f3 = Frame()
f4 = Frame()

l1 = Label(f1, text="Enter a Name: ")
e1 = Entry(f1, text="Name")

l2 = Label(f2, text="Enter a Body Part: ")
e2 = Entry(f2, text="Body Part")

l3 = Label(f3, text="Enter a Fluid: ")
e3 = Entry(f3, text="Fluid")

l4 = Label(f4, text="Enter a Substance: ")
e4 = Entry(f4, text="Substance")

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
t5 = StringVar()
t6 = StringVar()
t7 = StringVar()


def clickFunction():
    n1 = e1.get()
    v1.set(n1)

    n2 = e2.get()
    v2.set(n2)

    n3 = e3.get()
    v3.set(n3)

    n4 = e4.get()
    v4.set(n4)

    t1.set("is sick")
    t2.set("with the")
    t3.set("flu.")
    t4.set("Drink more")
    t5.set("and")
    t6.set("take")
    t7.set("as needed.")


b1 = Button(win, text="Click To Create Madlib", command=clickFunction)

mf1 = Frame()
ml1 = Label(mf1, textvariable=v1)
ml2 = Label(mf1, textvariable=t1)

mf2 = Frame()
ml3 = Label(mf2, textvariable=t2)
ml4 = Label(mf2, textvariable=v2)
ml5 = Label(mf2, textvariable=t3)

mf3 = Frame()
ml6 = Label(mf3, textvariable=t4)
ml7 = Label(mf3, textvariable=v3)
ml8 = Label(mf3, textvariable=t5)

mf4 = Frame()
ml9 = Label(mf4, textvariable=t6)
ml10 = Label(mf4, textvariable=v4)
ml11 = Label(mf4, textvariable=t7)

f1.pack()
l1.pack(side=LEFT)
e1.pack(side=LEFT)

f2.pack()
l2.pack(side=LEFT)
e2.pack(side=LEFT)

f3.pack()
l3.pack(side=LEFT)
e3.pack(side=LEFT)

f4.pack()
l4.pack(side=LEFT)
e4.pack(side=LEFT)

b1.pack()

mf1.pack()
ml1.pack(side=LEFT)
ml2.pack(side=LEFT)

mf2.pack()
ml3.pack(side=LEFT)
ml4.pack(side=LEFT)
ml5.pack(side=LEFT)

mf3.pack()
ml6.pack(side=LEFT)
ml7.pack(side=LEFT)
ml8.pack(side=LEFT)

mf4.pack()
ml9.pack(side=LEFT)
ml10.pack(side=LEFT)
ml11.pack(side=LEFT)

win.mainloop()
