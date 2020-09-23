from tkinter import *

class student_mentor:
    def __init__(self,root):
        self.root=root
        self.root.title("Online Student Managment")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Online Student Managment",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X) 
        button1=Button(self.root,text="MENTOR",font=('arial',20,'bold'),bd=10, height=1,width =10)
        button1.place(x=650,y=350)
        button2=Button(self.root,text="STUDENT",font=('arial',20,'bold'),bd=10, height=1,width=10)
        button2.place(x=650,y=430)
root=Tk()
ob=student_mentor(root)
root.mainloop()
