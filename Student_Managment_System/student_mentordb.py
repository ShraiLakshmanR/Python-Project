import sqlite3


def connectData():
    con=sqlite3.connect("student_mentordb.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS mentorlogin(student id TEXT NOT NULL PRIMARY KEY,fname TEXT NOT NULL,surname TEXT NOT NULL,dob TEXT NOT NULL,age NOT NULL,gender TEXT NOT NULL,address TEXT NOT NULL,mobile TEXT NOT NULL,college TEXT NOT NULL,course TEXT NOT NULL)""")
    con.commit()
    con.close()


def addStudentRecord(stdid,fname,surname,dob,age,gender,address,mobile,college,course):
     con=sqlite3.connect("student_mentordb.db")
     cur=con.cursor()
     cur.execute("""INSERT INTO student_mentordb VALUES(?,?,?,?,?,?,?,?,?,?)""",(stdid,fname,surname,dob,age,gender,address,mobile,college,course))
     con.commit()
     con.close()

