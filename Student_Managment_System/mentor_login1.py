import sqlite3


def connectData():
    con=sqlite3.connect("mentor_login1.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS mentorlogin(name TEXT NOT NULL,password INTEGER NOT NULL,address TEXT NOT NULL,state TEXT NOT NULL,addresscode NOT NULL,gender TEXT NOT NULL,mobileno REAL NOT NULL,department TEXT NOT NULL)""")
    con.commit()
    con.close()
    
def registeData(name,password,address,state,addresscode,gender,mobileno,department):
    con=sqlite3.connect("mentor_login1.db")
    cur=con.cursor()
    cur.execute("""INSERT INTO mentorlogin VALUES(?,?,?,?,?,?,?,?)""",(name,password,address,state,addresscode,gender,mobileno,department))
    con.commit()
    con.close()
    



connectData()



