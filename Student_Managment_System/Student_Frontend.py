
from tkinter import *
import tkinter.messagebox    #dilogue box opened
import  student_mentordb
from tkinter import ttk
import random
import time
import datetime





class outwindow:
    def __init__(self,root):       
        self.root=root
        self.root.title("Student")   
        self.root.geometry("1000x750+70+70")  
        self.root.config(bg="SlateGray4")


        MainFrame1=Frame(self.root,bg="cornsilk") 
        MainFrame1.pack(side=TOP)

        
        TitleFrame1=Frame(MainFrame1,bd=4,bg="Cornsilk",relief=RIDGE)
        TitleFrame1.pack(side=TOP)

        self.lblTit=Label(TitleFrame1,font=('Times New Roman',47,'bold'),text="Student Registeration ",bg="yellow",fg="red")
        self.lblTit.pack(side=TOP,fill=X)
        

        def reg():
            tkinter.messagebox.showinfo("student reg","Student Registeration")
            new_window()



        def disp():
            tkinter.messagebox.showinfo("student info","Student info display")
            new_window1()
            
            
            

        def new_window():
                newWindow=Toplevel(self.root)
                app=Student(newWindow)

        def new_window1():
                newWindow2=Toplevel(self.root)
                app1=Displaywindow(newWindow2)


        #===============================================BUTTONS=========================================================================#
        btn1=Button(self.root,text="Student Registeration",width=20,pady=5,font=("times new roman",25,"bold"),command=reg).place(relx = 0.5, rely =0.3 ,anchor = CENTER)
                                                                                                                             
        btn2=Button(self.root,text="Student Information",width=20,pady=5,font=("times new roman",25,"bold"),command=disp).place(relx = 0.5, rely =0.4, anchor = CENTER)

        quote="""\n\t   **INSTRUCTIONS STUDENTS**\n  REGISTERATION OF COURSE WHICH EVER YOU\n  ARE STUDYING.PLEASE FILL THE DETAILS CAREFULLY \n  NO FURTHER CHANGES CAN BE DONE.\n\n\t\t **THANKYOU**"""

        txt=Text(self.root,height=8, width=50,wrap=WORD,bg="black",fg="green2")
        txt.place(relx = 0.5, rely =0.7, anchor = CENTER)
        
        txt.insert(END, quote)
        #================================================functions=======================================================================================#
    





class Student:

    def __init__(self,root):       #roootisparentwindow
        self.root=root
        self.root.title("Student")   #title()string method-tkinterwindowname
        self.root.geometry("1000x750+70+70")  #to set dimension window
        self.root.config(bg="cadet blue")#bf-backgroundcolor
        


        StdID=StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        DOB=StringVar()             #holdsastring
        Age=StringVar()
        Gender=StringVar()
        Address=StringVar()
        Mobile=StringVar()
        Course=StringVar()
        Col=StringVar()
        Cgpa=DoubleVar()
        sem=StringVar()



         #===========================VALIDATION FUNCCC======================#
        def valid_data():
            if StdID.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Enter Student Id")
            elif Firstname.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please First name")
            elif Surname.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Surname")
            elif DOB.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Enter DOB")
            elif Age.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Enter Age ")
            elif Gender.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Enter Gender")
            elif Address.get()=="":
                 tkinter.messagebox.showinfo("WARNING","Please Enter Address")
            elif Mobile.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Enter Mobile No")
            elif Col.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Enter College")
            elif Course.get()=="":
                tkinter.messagebox.showinfo("WARNING","Please Enter Course")
        
            else:
                tkinter.messagebox.showinfo("Registeration Complete","Registered Succesfully")
                self.root.destroy()





        
        #===========================DATA BASE FUNCTIONS======================#

        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Managment System","Confirm if you want to exit")
            if iExit>0:
                root.destroy() #exit
                return


#        def clearData():
 #           self.txtStdID.delete(0,END)                 #CLEARING ALLL ENTRIES
  #          self.txtfname.delete(0,END)
   #         self.txtSurname.delete(0,END)
    #        self.txtDOB.delete(0,END)
     #       self.txtAge.delete(0,END)
      #      self.txtGender.delete(0,END)
       #      self.txtGender.delete(0,END)
        #    self.txtMobile.delete(0,END)
         #   self.comBoxC.delete(0,END)
          #  return
        def reset1():
                StdID.set("")                 #CLEARING ALLL ENTRIES
                Firstname.set("")
                Surname.set("")
                DOB.set("")
                Age.set("")
                Gender.set("")
                Address.set("")
                Mobile.set("")
                Course.set("")
                Col.set("")
                Cgpa.set("")
                sem.set("")
                self.txtStdID.focus()
             


        def studentRecord(event):
            global sd  
            searchStd= studentlist.curselection()[0]
            sd=studentlist.get(searchStd)

            self.txtStdID.delete(0,END)
            self.txtStdID.insert(END,sd[1])       
            self.txtfname.delete(0,END)
            self.txtfname.insert(END,sd[1])
            self.txtSurname.delete(0,END)
            self.txtSurname.insert(END,sd[1])
            self.txtDOB.delete(0,END)
            self.txtDOB.insert(END,sd[1])
            self.txtAge.delete(0,END)
            self.txtAge.insert(END,sd[1])
            self.txtGender.delete(0,END)
            self.txtGender.insert(END,sd[1])
            self.txtAddress.delete(0,END)
            self.txtAddress.insert(END,sd[1])
            self.txtMobile.delete(0,END)
            self.txtMobile.insert(END,sd[1])




        def addData():
            valid_data()
            sid=StdID.get()
            fname=Firstname.get()
            surname=Surname.get()
            dob=DOB.get()
            age=Age.get()
            gender=Gender.get()
            address=Address.get()
            mobile=Mobile.get()
            col=Col.get()
            course=Course.get()
            student_mentordb.addStudentRecord(sid,fname,surname,dob,age,gender,address,mobile,col,course)
            
            
               



        def displayData():
             studentlist.delete(0,END)
             for row in Student_Backend.viewData():
                 studentlist.insert(END,row,str=(""))


        def deleteData():
             if(len(StdID.get())!=0):
                  Student_Backend.deleteRec(sd[0])
                  clearData()
                  displayData()#sdglobalvariable

        def searchData():
            studentlist.delete(0,END)
            for row in Student_Backend.searchData(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()):
             studentlist.insert(END,row,str="")

        def update():
             if(len(StdID.get())!=0):
                  Student_Backend.deleteRec(sd[0])
             if(len(StdID.get())!=0):
                     Student_Backend.addStudentRecord(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(StdID.get(),Firstname.get(),Surname.get(),DOB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()))

                   

        #def Sid_no():
       
                #x=random.randint(1,100)
                #randommid=str(x)
                #str1="1BM17CS"+randommid
                #StdID.set(str1)






        
        #===========================FRAMES======================#
        MainFrame=Frame(self.root,bg="cadet blue") 
        MainFrame.pack(side=TOP)

        TitleFrame=Frame(MainFrame,  bd=6, padx=20, pady=8, bg="cadet blue",relief=RIDGE)#FRAME-outer and inner outer is changed to red
        TitleFrame.pack(side=TOP)
        
        self.lblTit=Label(TitleFrame,font=('Times New Roman',47,'bold'),text="Online Form",bg="yellow",fg="red")
        self.lblTit.grid(row=0,column=60,padx=30)


        ButtonFrame=Frame(MainFrame,  bd=2, width=400, height=70,padx=18,pady=10 ,bg="cadet blue",relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,  bd=1, width=1600, height=800,padx=20,pady=20, bg="cadet blue",relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=LabelFrame(DataFrame,bd=0, width=1200, height=800 ,padx=10, bg="Ghost white",relief=RIDGE,font=('Times New Roman',20,'bold'),text="  Student Information")
        DataFrameLEFT.pack(side=LEFT)

     #   DataFrameRIGHT=LabelFrame(DataFrame,bd=0, width=450, height=300 ,padx=3,pady=3, bg="Ghost white",relief=RIDGE,font=('Times New Roman',20,'bold'),text="    Student Details")
      #  DataFrameRIGHT.pack(side=RIGHT)


        #===========================LABELS and Entry==========================#
        self.lblStdID=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="Student ID:",padx=2,pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=StdID,width=25) #indataframeleftstudentid input taken
        self.txtStdID.grid(row=0,column=1)


        self.lblfname=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="First-Name:",padx=2,pady=2,bg="Ghost White")
        self.lblfname.grid(row=1,column=0,sticky=W)
        self.txtfname=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Firstname,width=25) #indataframeleftstudentid input taken
        self.txtfname.grid(row=1,column=1)



        self.lblSurname=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="Surname:",padx=2,pady=2,bg="Ghost White")
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtSurname=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Surname,width=25) #indataframeleftstudentid input taken
        self.txtSurname.grid(row=2,column=1)



        self.lblDOB=Label(DataFrameLEFT,font=('Times New Roman',18,'bold'),text="Date Of Birth :",padx=2,pady=2,bg="Ghost White")
        self.lblDOB.grid(row=3,column=0,sticky=W)
        self.txtDOB=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=DOB,width=25) #indataframeleftstudentid input taken
        self.txtDOB.grid(row=3,column=1)


        
        self.lblAge=Label(DataFrameLEFT,font=('Times New Roman',19,'bold'),text="Age:",padx=2,pady=2,bg="Ghost White")
        self.lblAge.grid(row=4,column=0,sticky=W)
        self.txtAge=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Age,width=25) #indataframeleftstudentid input taken
        self.txtAge.grid(row=4,column=1)



        self.lblGender=Label(DataFrameLEFT,font=('Times New Roman',18,'bold'),text="Gender(M/F):",padx=2,pady=2,bg="Ghost White")
        self.lblGender.grid(row=5,column=0,sticky=W)
        self.txtGender=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Gender,width=25) #indataframeleftstudentid input taken
        self.txtGender.grid(row=5,column=1)



        self.lblAddress=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="Address:",padx=2,pady=2,bg="Ghost White")
        self.lblAddress.grid(row=6,column=0,sticky=W)
        self.txtAddress=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Address,width=25) #indataframeleftstudentid input taken
        self.txtAddress.grid(row=6,column=1)


        self.lblMobile=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="Mobile:",padx=2,pady=2,bg="Ghost White")
        self.lblMobile.grid(row=7,column=0,sticky=W)
        self.txtMobile=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Mobile,width=25) #indataframeleftstudentid input taken
        self.txtMobile.grid(row=7,column=1)


        self.lblCol=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="College:",padx=2,pady=2,bg="Ghost White")
        self.lblCol.grid(row=8,column=0,sticky=W)
        self.txtCol=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Col,width=25) #indataframeleftstudentid input taken
        self.txtCol.grid(row=8,column=1)




       #self.lblCgpa=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="CGPA",padx=2,pady=2,bg="Ghost White")
        #self.lblCgpa.grid(row=9,column=0,sticky=W)
        #self.txtCgpa=Entry(DataFrameLEFT,font=('Times New Roman',17,'bold'),textvariable=Cgpa,width=25) #indataframeleftstudentid input taken
        #self.txtCgpa.grid(row=9,column=1)



        



        v=["AI","IOT","Python","ML","CON"]
        self.lblCourse=Label(DataFrameLEFT,font=('Times New Roman',20,'bold'),text="Course:",padx=2,pady=2,bg="Ghost White")
        self.lblCourse.grid(row=9,column=0,sticky=W)
        self.comBoxC=ttk.Combobox(DataFrameLEFT,width=26,textvariable=Course,values=v,font=("BOLD",15))
        self.comBoxC.grid(row=9,column=1)


       
        

        #===========================Listbox and ScrollBar==========================#

      #  scrollbar=Scrollbar(DataFrameRIGHT)
       # scrollbar.grid(row=0,column=1,sticky='ns')


        #studentlist=Listbox(DataFrameRIGHT,width=41,height=16,font=('Times New Roman',12,'bold'),yscrollcommand=scrollbar.set)
        #studentlist.bind('<<ListBoxSelect>>',studentRecord)
        #studentlist.grid(row=0,column=0,padx=8)
        #scrollbar.config(command=studentlist.yview)#y-axisview


        #===========================Button Widget==========================#


        #self.btnAddData=Button(ButtonFrame,text="Student-ID",font=('Times New Roman',17,'bold'),height=1,width=10,bd=4,command=Sid_no)
        #self.btnAddData.grid(row=0,column=0)


        self.btnAddData=Button(ButtonFrame,text="Submit",font=('Times New Roman',17,'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddData.grid(row=0,column=1)

       
        self.btnClearData=Button(ButtonFrame,text="Clear",font=('Times New Roman',17,'bold'),height=1,width=10,bd=4,command=reset1)
        self.btnClearData.grid(row=0,column=3)


        self.btnExit=Button(ButtonFrame,text="Exit",font=('Times New Roman',17,'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=4)


        





if __name__=='__main__':    #__name__isglobalvariableand__main__isthecurrentmodule
    root=Tk()
    application=outwindow(root)
    root.mainloop()   #mainloop is requied
