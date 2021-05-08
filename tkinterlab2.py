from tkinter import *
def credit(m):
    if(m=="A"):
        cred = 40
    elif(m=="B"):
        cred = 36
    elif(m=="C"):
        cred = 28
    elif(m=="D"):
        cred = 25
    else:
        cred="Enter A-D"
    return cred
def d1():
    m1=credit(e4.get())
    m2=credit(e5.get())
    m3=credit(e6.get())
    m4=credit(e7.get())
    maths.set(m1)
    physics.set(m2)
    chemistry.set(m3)
    english.set(m4)
    totalcredit.set(m1+m2+m3+m4)
    totalgrade.set((m1+m2+m3+m3)/4)
    
root=Tk()

root.title("Grade Calculator")
root.geometry("600x500")

maths = StringVar()
physics = StringVar()
chemistry = StringVar()
english = StringVar()
totalcredit = StringVar()
totalgrade = StringVar()


Label(root, text="Name").place(x=10, y=10)
Label(root, text="Roll.No").place(x=10, y=40)
Label(root, text="Reg.NO").place(x=220, y=20)

e1 = Entry(root)
e1.place(x=80, y=10)

e2 = Entry(root)
e2.place(x=80, y=40)

e3 = Entry(root)
e3.place(x=300, y=20)

Label(root, text="Srl.No").place(x=10,y=60)
Label(root, text="1").place(x=10,y=90)
Label(root, text="2").place(x=10,y=120)
Label(root, text="3").place(x=10,y=150)
Label(root, text="4").place(x=10,y=180)

Label(root, text="Subject").place(x=60,y=60)
lb1=Label(root, text="MATHS").place(x=60,y=90)
e4 = Entry(root)
e4.place(x=130,y=90)
lb2=Label(root, text="PHYSICS").place(x=60,y=120)
e5 = Entry(root)
e5.place(x=130,y=120)
lb3=Label(root, text="CHEMISTRY").place(x=60,y=150)
e6 = Entry(root)
e6.place(x=130,y=150)
lb4=Label(root, text="ENGLISH").place(x=60,y=180)
e7= Entry(root)
e7.place(x=130,y=180)

Label(root,text="GRADE").place(x=150,y=60)

Label(root, text="Sub Credit").place(x=300,y=60)
Label(root, text="1").place(x=320,y=90)
Label(root, text="2").place(x=320,y=120)
Label(root, text="3").place(x=320,y=150)
Label(root, text="4").place(x=320,y=180)

Label(root, text="Credit Obtained").place(x=400,y=60)

Label(root, text="Total Credit").place(x=300,y=210)
Label(root, text="Total Grade").place(x=300,y=240)

mat = Label(root, text="", textvariable=maths).place(x=420, y=90)
phy = Label(root, text="", textvariable=physics).place(x=420, y=120)
che = Label(root, text="", textvariable=chemistry).place(x=420, y=150)
eng = Label(root, text="", textvariable=english).place(x=420, y=180)

tc = Label(root, text="", textvariable=totalcredit).place(x=420, y=210)
tg = Label(root, text="", textvariable=totalgrade).place(x=420, y=240)

Button(root, text="Submit", command=d1 ,height = 1, width = 6, fg='black',bg='green').place(x=60, y=240)


root.mainloop()

