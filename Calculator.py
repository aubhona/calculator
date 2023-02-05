from tkinter import *

def summ():
    if inputt()[0]:
        a=int(inputt()[1])
        b=int(inputt()[2])
        lblAns.config(text=f"{a}+{b}={a+b}")

def diff():
    if inputt()[0]:
        a=int(inputt()[1])
        b=int(inputt()[2])
        lblAns.config(text=f"{a}-{b}={a-b}")

def mul():
    if inputt()[0]:
        a=int(inputt()[1])
        b=int(inputt()[2])
        lblAns.config(text=f"{a}*{b}={a*b}")

def div():
    if inputt()[0]:
        a=int(inputt()[1])
        b=int(inputt()[2])
        if b!=0:
            lblAns.config(text=f"{a}/{b}={int(a//b)}")
        else:
            lblAns.config(text='')
            
def inputt():
    a=edtA.get()
    b=edtB.get()
    qa=False
    qb=False
    if a!='':
        if a[0]=='-':
            a=a[1:]
            qa=True
    if b!='':
        if b[0]=='-' and b!='':
            b=b[1:]
            qb=True
    if a.isdecimal() and b.isdecimal():
        if qa:
            a='-'+a
        if qb:
            b='-'+b
        return [True, a, b]
    lblAns.config(text='Error!')
    return [False]
    
root=Tk()
root.geometry("200x180")
root.title("Calculator")
root.resizable(width=False, height=False) 

btnPlus=Button(root, text='+')
btnPlus.config(command=summ)
btnPlus.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.2)

btnMinus=Button(root, text='-')
btnMinus.config(command=diff)
btnMinus.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.2)

btnMul=Button(root, text='*')
btnMul.config(command=mul)
btnMul.place(relx=0.5, rely=0.4, relwidth=0.5, relheight=0.2)

btnDiv=Button(root, text='/' )
btnDiv.config(command=div)
btnDiv.place(relx=0.5, rely=0.6, relwidth=0.5, relheight=0.2)

edtA=Entry(width=10)
edtA.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.125)
edtB=Entry(width=10)
edtB.place(relx=0, rely=0.425, relwidth=0.5, relheight=0.125)

lblAns=Label(text="")
lblAns.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

root.mainloop()
