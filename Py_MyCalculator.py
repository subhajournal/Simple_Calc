#!/usr/bin/env python
# coding: utf-8

# In[48]:


from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter.font as font
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from win32api import GetSystemMetrics
from math import log


# In[94]:


w1="orchid1"
w2="deep pink"
w3="gold"
w4="lime green"
w5='salmon'
w6='blue violet'
w7='medium spring green'
w8='yellow2'
w9='brown1'
w10='medium spring green'
w11='snow'
w12='tomato'
w13='yellow2'
w14='hot pink'
w15='medium orchid'
w16='brown4'
sig="Calisto MT Bold"
expression=""
def syscalc():
    calc=Tk()
    calc.title("Calculator")
    calc.configure(bg=w11)
    style1 = Style() 
    style1.configure('W.TButton', font = 
               (sig, 10, 'bold'), 
                foreground = w6,borderwidth = '3') 

    calc.geometry(str(GetSystemMetrics(0)-1005)+'x'+str(GetSystemMetrics(1)-670))
    
    canvas = Canvas(width=500, height=300, bg=w11)
    canvas.pack(expand=YES, fill=BOTH)                

    canvas.create_rectangle(3, 5, 528, 60, width=1, fill=w11)
    
    calcshow=Label(calc, text="0              ",font=(sig,20))
    calcshow.place(x=10,y=10)
    calcshow.configure(foreground=w16,background=w11)

    equation = StringVar() 
    
    '''def result():
        for i in expression:
            print(i)'''
    
    def press(btn): 
        oprt=["^2"]
        global expression
        global btn1
        if btn not in oprt:
            if btn!="e":
                expression = expression + str(btn) 
                calcshow.configure(text=expression)
            else:
                try:
                    calcshow.configure(text=eval(expression))
                except ArithmeticError:
                    calcshow.configure(text="Math Error")
                except :
                    calcshow.configure(text="Incompatible Equation")
            if btn=="c":
                expression = "0"
                calcshow.configure(text=expression)
            
    
    add = Button(calc, text="+", command=lambda: press('+'), style = 'W.TButton').place(x=3,y=70)
    sub = Button(calc, text="-", command=lambda: press('-'),  style = 'W.TButton').place(x=89,y=70)
    mul = Button(calc, text="x", command=lambda: press('*'),  style = 'W.TButton').place(x=175,y=70)
    div = Button(calc, text="/", command=lambda: press('/'),  style = 'W.TButton').place(x=261,y=70)
    #pwr2 = Button(calc, text="x^y", command=lambda: press('^2'),  style = 'W.TButton').place(x=347,y=70)
    
    one = Button(calc, text="1", command=lambda: press('1'),  style = 'W.TButton').place(x=3,y=100)
    two = Button(calc, text="2", command=lambda: press('2'),  style = 'W.TButton').place(x=89,y=100)
    three = Button(calc, text="3", command=lambda: press('3'),  style = 'W.TButton').place(x=175,y=100)
    four = Button(calc, text="4", command=lambda: press('4'),  style = 'W.TButton').place(x=261,y=100)
    #pwr3 = Button(calc, text="x^x", command=lambda: press(''),  style = 'W.TButton').place(x=347,y=100)
    
    five = Button(calc, text="5", command=lambda: press('5'),  style = 'W.TButton').place(x=3,y=130)
    six = Button(calc, text="6", command=lambda: press('6'),  style = 'W.TButton').place(x=89,y=130)
    seven = Button(calc, text="7", command=lambda: press('7'),  style = 'W.TButton').place(x=175,y=130)
    eight = Button(calc, text="8", command=lambda: press('8'),  style = 'W.TButton').place(x=261,y=130)
    #pwrxy = Button(calc, text="x^y", command=lambda: press(''),  style = 'W.TButton').place(x=347,y=130)
    
    nine = Button(calc, text="9", command=lambda: press('9'),  style = 'W.TButton').place(x=3,y=160)
    z1 = Button(calc, text="0", command=lambda: press('0'),  style = 'W.TButton').place(x=89,y=160)
    z2 = Button(calc, text="00", command=lambda: press('00'),  style = 'W.TButton').place(x=175,y=160)
    point = Button(calc, text=".", command=lambda: press('.'),  style = 'W.TButton').place(x=261,y=160)
    #pwr10 = Button(calc, text="10^x", command=lambda: press(''),  style = 'W.TButton').place(x=347,y=160)
    
    '''root = Button(calc, text="root", command=lambda: press(''),  style = 'W.TButton').place(x=3,y=190)
    sin= Button(calc, text="sin", command=lambda: press(''),  style = 'W.TButton').place(x=89,y=190)
    cos = Button(calc, text="cos", command=lambda: press(''),  style = 'W.TButton').place(x=175,y=190)
    sec= Button(calc, text="sec", command=lambda: press('.'),  style = 'W.TButton').place(x=261,y=190)
    #tan = Button(calc, text="tan", command=lambda: press(''),  style = 'W.TButton').place(x=347,y=190)'''
    
    eql = Button(calc, text="=", command=lambda: press('e'),  style = 'W.TButton').place(x=351,y=70,width=177,height=72)
    ac = Button(calc, text="AC", command=lambda: press('c'),  style = 'W.TButton').place(x=351,y=145,width=177,height=42)
    
    
    calc.mainloop()
syscalc()
