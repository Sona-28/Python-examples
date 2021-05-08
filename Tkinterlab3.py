from tkinter import *
root = Tk()
def f1(n):
    num=""
    num=num+str(n)
    num.set(num)
Button(root, text="0",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(0)).place(x=30,y=90)
Button(root, text="1",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(1)).place(x=0,y=0)
Button(root, text="2",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(2)).place(x=30,y=0)
Button(root, text="3",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(3)).place(x=60,y=0)
Button(root, text="4",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(4)).place(x=0,y=30)
Button(root, text="5",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(5)).place(x=30,y=30)
Button(root, text="6",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(6)).place(x=60,y=30)
Button(root, text="7",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(7)).place(x=0,y=60)
Button(root, text="8",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(8)).place(x=30,y=60)
Button(root, text="9",height = 1, width = 2, fg='black',bg='green',command=lambda:f1(9)).place(x=60,y=60)
label=Label(root)
label.pack()
root.mainloop()
