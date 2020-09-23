from tkinter import *
import sqlite3
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import re
import mentor_login1


def main():
    root=Tk()
    app=Window1(root)




class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Login")
        self.master.geometry("720x750+2+2")
        self.master.config(bg='powder blue')
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()

        self.Username=StringVar()
        self.Password=StringVar()

        self.lblTitle=Label(self.frame,text="Student Mentor Login",bd=0,relief=RIDGE,font=('times new roman',30,'bold'),bg='powder blue',fg='black')
        self.lblTitle.grid(row=0,column=0,columnspan=5,pady=30)
        #===================FRAMES============================#
            
        self.LoginFrame1=LabelFrame(self.frame,width=1350,height=600,font=('arial',17,'bold'),relief='ridge',bg='cadet blue',bd=10)
        self.LoginFrame1.grid(row=1,column=0)


        self.LoginFrame2=LabelFrame(self.frame,width=1000,height=600,font=('arial',17,'bold'),relief='ridge',bg='cadet blue',bd=10)
        self.LoginFrame2.grid(row=2,column=0)
         #====================LABEL ENTRY==============================#
        self.lblUsername=Label(self.LoginFrame1,text="User-name:",font=('arial',18,'bold'),bd=22,bg='cadet blue',fg='Cornsilk')
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,textvariable=self.Username)
        self.txtUsername.grid(row=0,column=1)




        self.lblPassword=Label(self.LoginFrame1,text="Password:",font=('arial',19,'bold'),bd=22,bg='cadet blue',fg='Cornsilk')
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.LoginFrame1,show='*',textvariable=self.Password)
        self.txtPassword.grid(row=1,column=1)
        #====================Buttons========================#

                               
        self.btnLogin=Button(self.LoginFrame2,text='Login',width=8,font=('arial',15,'bold'),pady=20,padx=8,command=self.Login_system)
        self.btnLogin.grid(row=5,column=0)

        self.btnReset=Button(self.LoginFrame2,text='Reset',width=8,font=('arial',15,'bold'),pady=20,padx=8,command=self.reset)
        self.btnReset.grid(row=5,column=1)
        
        self.btnExit=Button(self.LoginFrame2,text='Exit',width=8,font=('arial',15,'bold'),pady=20,padx=8,command=self.iExit)
        self.btnExit.grid(row=5,column=2)


        self.btnRegister=Button(self.LoginFrame2,text='Register',width=8,font=('arial',15,'bold'),pady=20,padx=8,command=self.Register_system)
        self.btnRegister.grid(row=5,column=3)


        #====================Functions========================#
    def Login_system(self):
            
                n=self.Username.get()
                p=self.Password.get()
                con=sqlite3.connect("mentor_login1.db")
                cur=con.cursor()
                find_user=("""SELECT * FROM mentorlogin WHERE name= ? AND password= ?""")
                cur.execute(find_user,[(n),(p)])
                records=cur.fetchall()
                print(records)
                if records:
                    tkinter.messagebox.showinfo("mentor login","Welcome Mentor")
                    self.newWindow=Toplevel(self.master) 
                    self.app=Window2(self.newWindow)
                else:
                    tkinter.messagebox.showwarning("Mentor Login","Invalid user name or password")
                    self.reset()
                
            
       
        
            


    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        
            
    def Register_system(self):

           tkinter.messagebox.showinfo("Registration","MENTOR REGISTER")
           self.newWindow2=Toplevel(self.master)
           self.app1=Window3(self.newWindow2)


    def new_window(self):
           self.newWindow=Toplevel(self.master)
           self.app=Window2(self.newWindow)

    def new_window1(self):
           self.newWindow2=Toplevel(self.master)
           self.app1=Window3(self.newWindow2)
        

    def iExit(self):
            iExit=tkinter.messagebox.askyesno("Mentor Login","Confirm if you want to exit")
            if iExit>0:
                self.master.destroy() #exit
                return


    



class Window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Student Managment System")
        self.master.geometry("1350x750+0+0")
        self.master.config(bg='cadet blue')
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()

        #==========================================ALL VARIABLES========================#

        self.sname=StringVar()
        self.sid=StringVar()
        self.course=StringVar()
        self.cie1=StringVar()
        self.cie2=StringVar()
        self.cie3=StringVar()
        self.project=StringVar()
        self.lab=StringVar()
        self.remarks=StringVar()




         #=================================FRAMES======================================#

        title_lbl=Label(self.master,text="Online Student Managment",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title_lbl.pack(side=TOP,fill=X)
        


        Manage_Frame=Frame(self.master,bd=4,relief=RIDGE,bg="Cornsilk")
        Manage_Frame.place(x=20,y=160,width=450,height=600)

        m_title=Label(Manage_Frame,text="Manage Students",font=("times new roman",35,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="Cornsilk")
        btn_Frame.place(x=15,y=500,width=420)
        

        Detail_Frame=Frame(self.master,bd=4,relief=RIDGE,bg="Cornsilk")
        Detail_Frame.place(x=500,y=160,width=800,height=600)


        #=================================FRAMES======================================#

        #=================================DDFRAMES======================================#
        lbl_search=Label(Detail_Frame,text="Search By",font=("times new roman",17,"bold"))
        lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky="W")


        combo_search=ttk.Combobox(Detail_Frame,width=15,font=("times new roman",17,"bold"),state='readonly')
        combo_search['values']=("Course","Student-Id")
        combo_search.grid(row=0,column=1,padx=20,pady=10)


        txt_Search=Entry(Detail_Frame,width=15,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="W")



        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,font=("times new roman",8,"bold")).grid(row=0,column=3,padx=10,pady=10)
        showbtn=Button(Detail_Frame,text="Show ALL",width=10,pady=5,font=("times new roman",8,"bold")).grid(row=0,column=4,padx=10,pady=10)



        #=================================TableFRAMES======================================#



        table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE)
        table_Frame.place(x=10,y=70,width=760,height=500)




        
        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)
        Student_table=ttk.Treeview( table_Frame,columns=("Student Name","Student ID","Course"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("Student Name",text="Student-Name")
        Student_table.heading("Student ID",text="Student-Id")
        Student_table.heading("Course",text="Course")
        Student_table['show']='headings'
        Student_table.column("Student Name",width=50)
        Student_table.column("Student ID",width=100)
        Student_table.column("Course",width=100)

        Student_table.pack(fill=BOTH,expand=1)
        
        
        
        
                                   
        


























        #=================================TableFRAMES======================================#


        #=================================LABELS======================================#


        s_name_lbl=Label(Manage_Frame,text="Student Name:",font=("times new roman",17,"bold"))
        s_name_lbl.grid(row=1,column=0,pady=10,sticky="W")
        s_name_txt=Entry(Manage_Frame,textvariable=self.sname,font=("times new roman",15,"bold"))
        s_name_txt.grid(row=1,column=1,sticky="W")


        s_sid_lbl=Label(Manage_Frame,text="Student Id:",font=("times new roman",17,"bold"))
        s_sid_lbl.grid(row=2,column=0,pady=5,sticky="W")
        s_sid_txt=Entry(Manage_Frame,textvariable=self.sid,font=("times new roman",15,"bold"))
        s_sid_txt.grid(row=2,column=1,sticky="W")


        s_course_lbl=Label(Manage_Frame,text="Course:",font=("times new roman",17,"bold"))
        s_course_lbl.grid(row=3,column=0,pady=5,sticky="W")
        s_course_txt=Entry(Manage_Frame,textvariable=self.course,font=("times new roman",15,"bold"))
        s_course_txt.grid(row=3,column=1,sticky="W")




        s_cie1_lbl=Label(Manage_Frame,text="CIE-1 marks:",font=("times new roman",17,"bold"))
        s_cie1_lbl.grid(row=4,column=0,pady=5,sticky="W")
        s_cie1_txt=Entry(Manage_Frame,textvariable=self.cie1,font=("times new roman",15,"bold"))
        s_cie1_txt.grid(row=4,column=1,sticky="W")




        s_cie2_lbl=Label(Manage_Frame,text="CIE-2 marks:",font=("times new roman",17,"bold"))
        s_cie2_lbl.grid(row=5,column=0,pady=5,sticky="W")
        s_cie2_txt=Entry(Manage_Frame,textvariable=self.cie2,font=("times new roman",15,"bold"))
        s_cie2_txt.grid(row=5,column=1,sticky="W")





        s_cie3_lbl=Label(Manage_Frame,text="CIE-3 marks:",font=("times new roman",17,"bold"))
        s_cie3_lbl.grid(row=6,column=0,pady=5,sticky="W")
        s_cie3_txt=Entry(Manage_Frame,textvariable=self.cie3,font=("times new roman",15,"bold"))
        s_cie3_txt.grid(row=6,column=1,sticky="W")



        s_lab_lbl=Label(Manage_Frame,text="Lab-marks:",font=("times new roman",17,"bold"))
        s_lab_lbl.grid(row=7,column=0,pady=5,sticky="W")
        s_lab_txt=Entry(Manage_Frame,textvariable=self.lab,font=("times new roman",15,"bold"))
        s_lab_txt.grid(row=7,column=1,sticky="W")





        s_project_lbl=Label(Manage_Frame,text="Project-Assigned:",font=("times new roman",17,"bold"))
        s_project_lbl.grid(row=8,column=0,pady=5,sticky="W")
        s_project_txt=Entry(Manage_Frame,textvariable=self.project,font=("times new roman",15,"bold"))
        s_project_txt.grid(row=8,column=1,sticky="W")



        s_remark_lbl=Label(Manage_Frame,text="Remarks:",font=("times new roman",17,"bold"))
        s_remark_lbl.grid(row=9,column=0,pady=5,sticky="W")
        s_remark_lbl=Entry(Manage_Frame,textvariable=self.remarks,font=("times new roman",15,"bold"))
        s_remark_lbl.grid(row=9,column=1,sticky="W")

        

        #=================================LABELS======================================#


        #=================================BUTTONS======================================#

        addbtn=Button(btn_Frame,text="ADD",width=10,font=("times new roman",8,"bold")).grid(row=0,column=1,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="UPDATE",width=10,font=("times new roman",8,"bold")).grid(row=0,column=2,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="DELETE",width=10,font=("times new roman",8,"bold")).grid(row=0,column=3,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="CLEAR",width=10,font=("times new roman",8,"bold")).grid(row=0,column=4,padx=10,pady=10)


        #=================================BUTTONS======================================#


#============================================CLASS2 END===========================================#
class Window3:
    def __init__(self,master):
        self.master=master
        self.master.title("Mentor Regestration")
        self.master.geometry("1000x750+0+0")
        self.master.config(bg='cadet blue')
        self.frame=Frame(self.master,bg='powder blue')
        self.frame.pack()

        
        self.fname=StringVar()
        self.mid=StringVar()
        self.Addr=StringVar()
        self.addrcode=StringVar()
       # self.city=StringVar() #notadded to be added
        self.mno=StringVar()
        self.sex=StringVar()
        self.dep=StringVar()
        self.state=StringVar()
       
        
        

       #===================================FRAMES==================================================#

        winFrame=Frame(self.master,bg="cadet blue") 
        winFrame.pack(side=TOP)

        TitleFrame=Frame(winFrame,bd=3, padx=10, pady=3, bg="cadet blue",relief=RIDGE)#FRAME-outer and inner outer is changed to red
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=("Arial",59,"bold"),fg="red",text="Mentor Regestration",bg="yellow")
        self.lblTitle.pack(side=TOP,fill=X)
       

        MentorFrame=LabelFrame(winFrame,width=1000,height=500,bd=3,pady=2,relief=RIDGE)
        MentorFrame.pack(side=TOP)



        ButFrame=LabelFrame(winFrame,width=600,height=300,font=('arial',17,'bold'),relief='ridge',bg='cadet blue',bd=2)
        ButFrame.pack(side=BOTTOM)








       #====================================LABELS========================================#

        self.lblUsername=Label(MentorFrame,text="Name:",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=2,pady=20)
        self.lblUsername.grid(row=0,column=0,sticky=W)
        self.txtUsername=Entry(MentorFrame,textvariable=self.fname,font=('arial',10,'bold'),insertwidth=3)
        self.txtUsername.grid(row=0,column=1,sticky=W)


        self.lblmid=Label(MentorFrame,text="Mentor-ID:",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=2,pady=20)
        self.lblmid.grid(row=1,column=0,sticky=W)
        self.txtmid=Entry(MentorFrame,textvariable=self.mid,font=('arial',10,'bold'),state=DISABLED,insertwidth=3)   #STATEDISABLEDLOCKSENTRY
        self.txtmid.grid(row=1,column=1,sticky=W)


        self.lblAddr=Label(MentorFrame,text="Address 1:",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=2,pady=20)
        self.lblAddr.grid(row=2,column=0,sticky=W)
        self.txtAddr=Entry(MentorFrame,textvariable=self.Addr,font=('arial',10,'bold'),insertwidth=3)
        self.txtAddr.grid(row=2,column=1,sticky=W)



        self.lblAddr=Label(MentorFrame,text="State:",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=2,pady=20)
        self.lblAddr.grid(row=3,column=0,sticky=W)
        self.txtState=Entry(MentorFrame,textvariable=self.state,font=('arial',10,'bold'),insertwidth=3)
        self.txtState.grid(row=3,column=1,sticky=W)

        


        self.lbladdrcode=Label(MentorFrame,text="Address Code:",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=2,pady=20)
        self.lbladdrcode.grid(row=4,column=0,sticky=W)
        self.txtaddrcode=Entry(MentorFrame,textvariable=self.addrcode,font=('arial',10,'bold'),insertwidth=3)
        self.txtaddrcode.grid(row=4,column=1,sticky=W)






        self.lblsex=Label(MentorFrame,text="Gender(M/F)",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=10,pady=20)
        self.lblsex.grid(row=5,column=0,sticky=W)
        self.txtsex=Entry(MentorFrame,textvariable=self.sex,font=('arial',10,'bold'),insertwidth=3)
        self.txtsex.grid(row=5,column=1,sticky=W)







        self.lblmno=Label(MentorFrame,text="Mobile no:",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=10,pady=20)
        self.lblmno.grid(row=6,column=0,sticky=W)
        self.txtmno=Entry(MentorFrame,textvariable=self.mno,font=('arial',10,'bold'),insertwidth=3)
        self.txtmno.grid(row=6,column=1,sticky=W)


         

        v=["AI","IOT","Python","ML","CON"]
        self.lblbox=Label(MentorFrame,text="Department:",font=('arial',20,'bold'),bd=2,bg='#F0F0F0',fg='black',padx=10,pady=20)
        self.lblbox.grid(row=9,column=0,sticky=W)
        self.comBox=ttk.Combobox(MentorFrame,width=25,textvariable=self.dep,values=v,font=("BOLD",10))
        self.comBox.grid(row=9,column=1,sticky=W)

    #========================================BUTTON========================================#
        self.btnReset=Button(ButFrame,text='Reset',width=10,font=('arial',14,'bold'),pady=2,padx=2,command=self.reset1)
        self.btnReset.grid(row=0,column=2,sticky=W)

        
        self.btnExit=Button(ButFrame,text='Exit',width=10,font=('arial',14,'bold'),pady=2,padx=2,command=self.iExit)
        self.btnExit.grid(row=0,column=3,sticky=W)


        self.btnReg=Button(ButFrame,text='Register',width=10,font=('arial',14,'bold'),pady=2,padx=2,command=self.registerData)
        self.btnReg.grid(row=0,column=1,sticky=W)




        self.btnmid=Button(ButFrame,text='MID',width=10,font=('arial',14,'bold'),pady=2,padx=2,command=self.Mid_no)
        self.btnmid.grid(row=0,column=0,sticky=W)


     #===========================================FUNCTIONS==========================================#
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Mentor Register","Confirm if you want to exit")
        if iExit>0:
             self.master.destroy() #exit
             return



    def reset1(self):

        self.fname.set("")
        self.mid.set("")
        self.Addr.set("")
        self.addrcode.set("")
        #self.city.set("")
        self.mno.set("")
        self.sex.set("")
        self.dep.set("")
        self.state.set("")
        self.txtUsername.focus()


    def Mid_no(self):
            self.x=random.randint(1000,5000)
            self.randommid=str(self.x)
            self.mid.set(self.randommid)
        
            
           
       
            
            

         #===========================================FUNCTIONSVVALIDATION==========================================#
    def valid_data(self):
        if self.fname.get()=="":
            tkinter.messagebox.showinfo("WARNING","Please Enter Name")
        elif self.mid.get()=="":
            tkinter.messagebox.showinfo("WARNING","Please Click MID Button")
        elif self.Addr.get()=="":
            tkinter.messagebox.showinfo("WARNING","Please Enter Address")
        elif self.state.get()=="":
            tkinter.messagebox.showinfo("WARNING","Please Enter State")
        elif self.addrcode.get()=="":
            tkinter.messagebox.showinfo("WARNING","Please Enter Code ")
        elif self.sex.get()=="":
            tkinter.messagebox.showinfo("WARNING","Please Enter Sex")
        elif self.mno.get()=="":
             tkinter.messagebox.showinfo("WARNING","Please Enter Mobile No")
        elif self.dep.get()=="":
            tkinter.messagebox.showinfo("WARNING","Please Enter Department")
        
   
        else:
            tkinter.messagebox.showinfo("Registeration Complete","Registered Succesfully")
            self.master.destroy()

            
                
        
        
     #===========================================DATABASE-FUNCTIONS=============================================#


    def registerData(self):
        self.valid_data()
        self.uname=self.fname.get()
        self.mid=self.mid.get()
        self.addr=self.Addr.get()
        self.state=self.state.get()
        self.addrcode=self.addrcode.get()
        self.sex=self.sex.get()
        self.mno=self.mno.get()
        self.comBox=self.dep.get()
        mentor_login1.registeData(self.uname,self.mid,self.addr,self.state,self.addrcode,self.sex,self.mno,self.comBox)
    
            
        



      #=========================================================================================================#  

if __name__=='__main__':
    main()
