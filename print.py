from tkinter import *
from tkinter import messagebox
def btn1():
    print("Hello")
def btn2():
    if v.get()=="1":
        print('Welcome to India')
        return "1"
def btn3():
    if v.get()=="2":
        print("Welcome to USA")
        return "2"
def btn4():
    if v.get()=="3":
        print("Welcome")
        return "3"
root=Tk()
v= StringVar()
v.set(1)
frame=Frame(root)
label1= Label(root,text="Firstname")
label1.pack()
entry1=Entry(root)
entry1.pack()
label2=Label(root,text="Lastname")
label2.pack()
entry2=Entry(root)
entry2.pack()
label3=Label(root,text="Email ID")
label3.pack()
entry3=Entry(root)
entry3.pack()
country={"India" : "1", "USA" : "2", "Others" : "3"}
for (text,country) in country.items():
    rd1=Radiobutton(root, text=text, variable=v, value=country)
    rd1.pack()
bn1=Button(frame,text="Button1",command=btn1)
bn1.pack(side=RIGHT,padx=5)
bn2=Button(frame,text="Button2",command=btn2)
bn2.pack(side=TOP,padx=5)
bn3=Button(frame,text="Button3",command=btn3)
bn3.pack(side=LEFT,padx=5)
bn4=Button(frame,text="Button4",command=btn4)
bn4.pack(side=BOTTOM,padx=5)
frame.pack()
root.mainloop()
