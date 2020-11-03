"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the fac tored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()

bv = StringVar()
bv.set("b")
cv = StringVar()
cv.set("c")
ov = StringVar()
ov.set("Output goes here")

sign1 = StringVar()
sign1.set("-")
sign2 = StringVar()
sign2.set("+")


def factorFun():
    cs3 = sign1.get()
    cs4 = sign2.get()

    a = 1

    if cs3 == "-":
        b = -int(l4.get())
    elif cs3 == "+":
        b = int(l4.get())

    if cs4 == "-":
        c = -int(l6.get())
    elif cs4 == "+":
        c = int(l6.get())

    o1 = (-b + (b**2 - 4*a*c)**(1/2)) / 2
    o2 = (-b - (b**2 - 4*a*c)**(1/2)) / 2

    o1b = -1*o1
    o2b = -1*o2

    pa = str(o1b)
    na = str(o2b)

    if o1b > 0 and o2b > 0:
        fform = "(x + " + pa + ")" + "(x + " + na + ")"
    elif o1b > 0 and o2b < 0:
        fform = "(x + " + pa + ")" + "(x" + na + ")"
    elif o1b < 0 and o2b < 0:
        fform = "(x" + pa + ")" + "(x" + na + ")"
    elif o1b < 0 and o2b > 0:
        fform = "(x" + pa + ")" + "(x + " + na + ")"

    l8.delete(0, END)
    l8.insert(0, fform)


def sc1():
    cs = sign1.get()
    if cs == "-":
        sign1.set("+")
    elif cs == "+":
        sign1.set("-")


def sc2():
    cs2 = sign2.get()
    if cs2 == "-":
        sign2.set("+")
    elif cs2 == "+":
        sign2.set("-")


f1 = Frame()

l1 = Label(win, text='INPUT VALUES FOR "b" and "c", THEN PRESS THE BUTTON TO FACTOR THE TRINOMIAL', bg="#aaffff")
l1b = Label(win, text="TOGGLE SIGNS BY PRESSING THEM", bg="#aaffff")
l2 = Label(
    win, text='FOR THE PURPOSES OF THE PROGRAM, "a" WILL ALWAYS EQUAL 1', bg="#aaffff")

l3 = Label(f1, text="ax^2")
l3b = Button(f1, textvariable=sign1, command=sc1)
l4 = Entry(f1, text="b", textvariable=bv, width=2)
l5 = Label(f1, text="x")
l5b = Button(f1, textvariable=sign2, command=sc2)
l6 = Entry(f1, text="c", textvariable=cv, width=2)

l7 = Button(win, text="FACTOR TRINOMIAL", command=factorFun)

l8 = Entry(win, text="output", textvariable=ov)

l1.pack()
l1b.pack()
l2.pack()

f1.pack()
l3.pack(side=LEFT)
l3b.pack(side=LEFT)
l4.pack(side=LEFT)
l5.pack(side=LEFT)
l5b.pack(side=LEFT)
l6.pack(side=LEFT)

l7.pack()
l8.pack()

win.mainloop()

print()
