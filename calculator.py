from tkinter import *
from math import *
import sys,os
relative_path='dist\\4.png'
def resource_path(relative_path):
         if hasattr(sys,'_MEIPASS'):
                 return os.path.join(sys._MEIPASS,relativepath)
         return os.path.join(os.path.abspath("."),relative_path)

x=0

def  show():
        global x
        E1.insert(x,chr(48))
        x=x+1
        print (x)




def  show1():
            global x
            E1.insert(x, 1)
            x = x + 1




def show2():
    global x
    E1.insert(x, 2)
    x=x+1

def show3():
    global x
    E1.insert(x, 3)
    x=x+1

def show4():
    global x
    E1.insert(x, 4)
    x=x+1

def show5():
    global x
    E1.insert(x, 5)
    x=x+1

def show6():
    global x
    E1.insert(x, 6)
    x=x+1

def show7():
    global x
    E1.insert(x, 7)
    x=x+1

def show8():
    global x
    E1.insert(x, 8)
    x=x+1

def show9():
    global x
    E1.insert(x, 9)
    x=x+1

def show10(): #for addition
    global x
    E1.insert(x,chr(43))
    x=x+1
def show11(): # for subtraction
    global x
    E1.insert(x,chr(45))
    x=x+1
def show12(): # for multiplication
    global x
    E1.insert(x,chr(42))
    x=x+1
def show13():# for division
    global x
    E1.insert(x,chr(47))
    x=x+1
def squareroot():# for squareroot
  global x

  u=sqrt(float(E1.get()))

  E1.delete(0, END)
  m=round(u,2)
  E1.insert(0, m)
  x=x+1
def logarithmbase10():
    global x
    u=log10(float(E1.get()))
    E1.delete(0, END)
    m = round(u, 2)
    E1.insert(0, m)
    x = x + 1
def logarithmbase2():
    global x
    u=log2(float(E1.get()))
    E1.delete(0, END)
    m = round(u, 2)
    E1.insert(0, m)
    x = x + 1
def exponent():
    global x
    u=exp(float(E1.get()))
    E1.delete(0, END)
    m = round(u, 2)
    E1.insert(0, m)
    x = x + 1
def square():
    global x
    u=float(E1.get())
    t=u*u
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def cube():
    global x
    u=float(E1.get())
    t=u*u*u
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def sine():
    global x
    u=sin(float(E1.get()))
    t=round(u,2)
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def cosine():
    global x
    u=cos(float(E1.get()))
    t=round(u,2)
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def tangent():
    global x
    u=tan(float(E1.get()))
    t=round(u,2)
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def sineh():
    global x
    u=sinh(float(E1.get()))
    t=round(u,2)
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def cosineh():
    global x
    u=cosh(float(E1.get()))
    t=round(u,2)
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def tangenth():
    global x
    u=tanh(float(E1.get()))
    t=round(u,2)
    E1.delete(0, END)

    E1.insert(0, t)
    x = x + 1
def factorial1():
    global x
    u=factorial(float(E1.get()))

    E1.delete(0, END)

    E1.insert(0, u)
    x = x + 1

def point():

    global x
    E1.insert(x, chr(46))
    x = x + 1
    print(x)





def result():


    t=eval(E1.get())

    E1.delete(0,END)
    E1.insert(0,t)
    print(t)

def clear():

    E1.delete(0,END)



if __name__=='__main__':
    x=0

    root=Tk()
    root.title("faisal-calculator")
    #root.frame("300x500")
    back= Frame(master=root, width=0, height=0)
    root.resizable(width=False, height=False)
    imagePath = PhotoImage(file="dist\\4.png")
    widgetf = Label(root, image=imagePath).pack(side='left')


    # labels can be text or images



    l_1 = Label(root, text="Developed By", font=('Times', 21))
    l_2 = Label(root, text="Faisal", font=('Times', 21))
    l_3=Label(root, text="SIMPLE CALCULATOR",font=('Times',20))
    button=Button(root,text="0",width=5, height=3,command=show,background='black',fg='white')
    button1=Button(root,text="1",width=5, height=3,command=show1,background='black',fg='white')
    button2=Button(root,text="2",width=5, height=3,command=show2,background='black',fg='white')
    button3=Button(root,text="3",width=5, height=3,command=show3,background='black',fg='white')
    button4=Button(root,text="4",width=5, height=3,command=show4,background='black',fg='white')
    button5=Button(root,text="5",width=5, height=3,command=show5,background='black',fg='white')
    button6=Button(root,text="6",width=5, height=3,command=show6,background='black',fg='white')
    button7=Button(root,text="7",width=5, height=3,command=show7,background='black',fg='white')
    button8=Button(root,text="8",width=5, height=3,command=show8,background='black',fg='white')
    button9=Button(root,text="9",width=5, height=3,command=show9,background='black',fg='white')
    button10=Button(root,text="+",width=6, height=3,command=show10,background='red',fg='white')
    button11=Button(root,text="-",width=6, height=3,command=show11,background='red',fg='white')
    button12=Button(root,text="*",width=6, height=3 ,command=show12,background='red',fg='white')
    button13=Button(root,text="/",width=6, height=3 ,command=show13,background='red',fg='white')
    button14=Button(root,text="=",width=5, height=3,command=result,background='black',fg='white')
    button15 = Button(root, text="clear all ", width=6, height=3, command=clear,background='red',fg='white')
    button16 = Button(root, text="square root", width=10, height=1, command=squareroot)
    button17 = Button(root, text="log10", width=10, height=1, command=logarithmbase10)
    button18 = Button(root, text="log2", width=10, height=1, command=logarithmbase2)
    button19 = Button(root, text="exponent", width=10, height=1, command=exponent)
    button20 = Button(root, text="square", width=10, height=1, command=square)
    button21 = Button(root, text="cube", width=10, height=1, command=cube)
    button22 = Button(root, text="sine", width=10, height=1, command=sine)
    button23 = Button(root, text="cosine", width=10, height=1, command=cosine)
    button24 = Button(root, text="tangent", width=10, height=1, command=tangent)
    button25 = Button(root, text="sine hyperbolic", width=10, height=1, command=sineh)
    button26 = Button(root, text="cosine hyperbolic", width=10, height=1, command=cosineh)
    button27 = Button(root, text="tangent hyperbolic", width=10, height=1, command=tangenth)
    button28 = Button(root, text="factorial", width=10, height=1, command=factorial1)
    button29 = Button(root, text=".", width=5, height=3, command=point,background='black',fg='white')

    E1=Entry( root)
    E1.config(justify=RIGHT,width=10,font=('arial',21))
    l_1.place(x=0, y=20)
    l_2.place(x=0, y=50)
    l_3.place(x=0,y=100)
    E1.place(x=100,y=190)
    button.place(x=100,y=430)
    button1.place(x=100,y=370)
    button2.place(x=150, y=370)
    button3.place(x=200, y=370)
    button4.place(x=100, y=310)
    button5.place(x=150, y=310)
    button6.place(x=200, y=310)
    button7.place(x=100, y=250)
    button8.place(x=150, y=250)
    button9.place(x=200, y=250)
    button29.place(x=150, y=430)
    button14.place(x=200,y=430)
    button10.place(x=20, y=370)
    button11.place(x=20, y=310)
    button12.place(x=20, y=250)
    button13.place(x=20, y=430)
    button15.place(x=20, y=190)


   # button16.place(x=500, y=50)
   # button17.place(x=500, y=80)
    #button18.place(x=500, y=110)
    #button19.place(x=500, y=140)
   #button20.place(x=500, y=170)
   # button21.place(x=500, y=200)
   # button22.place(x=500, y=230)
   # button23.place(x=500, y=260)
   # button24.place(x=500, y=290)
   # button25.place(x=500, y=320)
   # button26.place(x=500, y=350)
  #  button27.place(x=500, y=380)
  # button28.place(x=500, y=410)
    back.pack()
    mainloop()

