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


def factorFun():
    a = 1
    b = int(l4.get())
    c = int(l6.get())

    o1 = ( -b + ( b**2 - 4*a*c )**(1/2) ) / 2
    o2 = ( -b - ( b**2 - 4*a*c )**(1/2) ) / 2

    pa = str(-1*o1)
    na = str(-1*o2)
    fform = "(x + " + pa + ")" + "(x + " + na + ")"
    
    l8.delete(0,END)
    l8.insert(0,fform)

f1 = Frame()

l1 = Label(win, text='INPUT VALUES FOR "b" and "c", THEN PRESS THE BUTTON TO FACTOR THE TRINOMIAL', bg="#aaffff")
l2 = Label(win, text='FOR THE PURPOSES OF THE PROGRAM, "a" WILL ALWAYS EQUAL 1', bg="#aaffff")

l3 = Label(f1, text="ax^2 +")
l4 = Entry(f1, text="b", textvariable=bv, width=2)
l5 = Label(f1, text="x +")
l6 = Entry(f1, text="c", textvariable=cv, width=2)

l7 = Button(win, text="FACTOR TRINOMIAL", command=factorFun)

l8 = Entry(win, text="output", textvariable=ov)

l1.pack()
l2.pack()

f1.pack()
l3.pack(side=LEFT)
l4.pack(side=LEFT)
l5.pack(side=LEFT)
l6.pack(side=LEFT)

l7.pack()
l8.pack()

win.mainloop()

