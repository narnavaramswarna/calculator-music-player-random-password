import tkinter
from tkinter import*
root=Tk()
root.title("\U0001F600 SIMPLE CALCULATOR \U0001F600")
root.geometry("570x700")
root.resizable(False,False)
root.configure(bg="green")
equation =" "

def show(value):
    global equation
    equation+=value
    label.config(text=equation)

def clear():
    global equation
    equation=" "
    label.config(text=equation)    

def calculate():
    global equation
    result=" "
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label.config(text=result) 

def ready():
    global equation
    result=""
      

def exit():
    clear()
    

label=Label(root,width=30,height=2,text="",font=("technology",29))
label.pack()

Button(root,text="c",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="blue",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="violet",command=lambda:show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="green",command=lambda:show("-")).place(x=430,y=200)

Button(root,text="4",width=4,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("4")).place(x=10,y=300)
Button(root,text="5",width=4,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("5")).place(x=150,y=300)
Button(root,text="6",width=4,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("6")).place(x=290,y=300)
Button(root,text="+",width=4,height=1,font=("technology",29,"italic"),bd=1,fg="grey",bg="white",command=lambda:show("+")).place(x=430,y=300)

Button(root,text="1",width=4,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("1")).place(x=10,y=400)
Button(root,text="2",width=4,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("2")).place(x=150,y=400)
Button(root,text="3",width=4,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("3")).place(x=290,y=400)
Button(root,text="0",width=11,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show("0")).place(x=10,y=500)

Button(root,text=".",width=5,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3,font=("technology",29,"italic"),bd=1,fg="white",bg="orange",command=lambda:calculate()).place(x=430,y=415)

Button(root,text="OFF",width=10,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="grey",command=lambda:exit()).place(x=10,y=600)
Button(root,text="ON",width=10,height=1,font=("technology",29,"italic"),bd=1,fg="white",bg="orange",command=lambda:ready()).place(x=250,y=600)
root.mainloop()
