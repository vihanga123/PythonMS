
"""
import tkinter
import sqlite3
from sqlite3 import Connection
from tkinter import *

# table
conn: Connection = sqlite3.connect('test1.db')

conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT)")
# conn.execute("INSERT INTO users (username,password) VALUES('vihanga','123')")
conn.commit()
print("Success", "User added successfully!")


def clear():
    user.delete(0, tkinter.END)
    password.delete(0, tkinter.END)


top = Tk()
top.title("Student LMS")
# top.geometry("300x200")
heading = tkinter.Label(text="Login Form", background="#34A2FE", foreground="white")
heading.grid(row=0, column=2)

label = tkinter.Label(text="Insert Name: ")
label.grid(row=2, column=1)
user = tkinter.Entry()
user.grid(row=2, column=2)

label = tkinter.Label(text="Insert Password: ")
label.grid(row=4, column=1)
password = tkinter.Entry(show="*")
password.grid(row=4, column=2)

button2 = tkinter.Button(text='clear', command=clear)
button2.grid(row=5, column=2)


def login():
    uname = user.get()
    pw = password.get()

    cursor = conn.execute("SELECT username,password FROM users WHERE username=? AND password=? ", [uname, pw])
    users = cursor.fetchone()

    if users is not None and users[0] == uname:
        if users is not None and users[1] == password:
            print("Login Failed")
        else:
            print("Login Successful")
            dashboard()
    else:
        print("Login Failed")


def dashboard():
    dash = tkinter.Toplevel(top)
    dash.title("Dashboard")
    dash.geometry("600x200")
    dashhead = tkinter.Label(dash, text="Dashboard", background="#34A2FE", foreground="white")
    dashhead.grid(row=0, column=2)

    regStudent = tkinter.Button(dash, text='Register a Student', command=StudentReg)
    regStudent.grid(row=2, column=1)
    showStudent = tkinter.Button(dash, text='See details of a Student', command=ViewStudent)
    showStudent.grid(row=2, column=2)
    regStaff = tkinter.Button(dash, text='Register a Staff member', command=RegStaff)
    regStaff.grid(row=3, column=1)
    showStaff = tkinter.Button(dash, text='See details of a Staff member', command=ViewStaff)
    showStaff.grid(row=3, column=2)

    dash.grab_set()


button = tkinter.Button(text="Input", command=login)
button.grid(row=5, column=1)


def StudentReg():
    conn.execute("CREATE TABLE IF NOT EXISTS student (Sid INTEGER PRIMARY KEY ,name TEXT,age INTEGER, pathway TEXT)")

    StudentReg = tkinter.Toplevel(top)
    StudentReg.title("Student Registration")
    StudentReg.geometry("600x200")
    StudentReghead = tkinter.Label(StudentReg, text="Student Registration", background="#34A2FE", foreground="white")
    StudentReghead.grid(row=0, column=2)

    label = tkinter.Label(StudentReg, text="Student ID: ")
    label.grid(row=2, column=1)
    Uid = tkinter.Entry(StudentReg)
    Uid.grid(row=2, column=2)

    label = tkinter.Label(StudentReg, text="Student Name: ")
    label.grid(row=3, column=1)
    Sname = tkinter.Entry(StudentReg)
    Sname.grid(row=3, column=2)

    label = tkinter.Label(StudentReg, text="Student Age: ")
    label.grid(row=4, column=1)
    Sage = tkinter.Entry(StudentReg)
    Sage.grid(row=4, column=2)

    label = tkinter.Label(StudentReg, text="Student Pathway: ")
    label.grid(row=5, column=1)
    pathway = tkinter.Entry(StudentReg)
    pathway.grid(row=5, column=2)

    cursor = conn.execute("SELECT * FROM student")
    data = cursor.fetchall()

    for info in data:
        print(info)

    StudentReg.grab_set()

    def AddStudent():
        Uidint = int(Uid.get())
        sname = Sname.get()
        Sageint = int(Sage.get())
        spathway = pathway.get()
        conn.execute("INSERT INTO student (Sid,name,age,pathway) VALUES (?, ?, ?, ?)",
                     [Uidint, sname, Sageint, spathway])
        print("Student Registered Successfully")

    register = tkinter.Button(StudentReg, text="Register", command=AddStudent)
    register.grid(row=6, column=2)


def ViewStudent():
    ViewStudent = tkinter.Toplevel(top)
    ViewStudent.title("View Student Details")
    ViewStudent.geometry("600x200")
    ViewStudenthead = tkinter.Label(ViewStudent, text="View Student Details", background="#34A2FE", foreground="white")
    ViewStudenthead.grid(row=0, column=2)

    ViewStudent.grab_set()


def RegStaff():
    conn.execute("CREATE TABLE IF NOT EXISTS staff (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT,password TEXT)")
    RegStaff = tkinter.Toplevel(top)
    RegStaff.title("Register Staff")
    RegStaff.geometry("600x200")
    RegStaffhead = tkinter.Label(RegStaff, text="Register Staff", background="#34A2FE", foreground="white")
    RegStaffhead.grid(row=0, column=2)

    RegStaff.grab_set()


def ViewStaff():
    ViewStaff = tkinter.Toplevel(top)
    ViewStaff.title("View Staff Details")
    ViewStaff.geometry("600x200")
    ViewStaffhead = tkinter.Label(ViewStaff, text="View Staff Details", background="#34A2FE", foreground="white")
    ViewStaffhead.grid(row=0, column=2)

    ViewStaff.grab_set()


top.mainloop()
conn.close()
"""

import sys
import sqlite3
from sqlite3 import Connection
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QPushButton, QWidget
#from RegForm import register
from Login import stafflogin

conn: Connection = sqlite3.connect('Main.db')

conn.execute("CREATE TABLE IF NOT EXISTS Registration (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,DOB DATE,occupation TEXT,username TEXT,password TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,address TEXT,telephone INTEGER,course TEXT)")
# conn.execute("INSERT INTO users (username,password) VALUES('vihanga','123')")
conn.commit()
print("Database is running!")

cursor = conn.cursor()
#Prints Registration entries
cursor.execute("SELECT * FROM Registration")
rows = cursor.fetchall()
#for row in rows:
print(rows)

#Prints Student entries
cursor.execute("SELECT * FROM Student")
stud = cursor.fetchall()
#for row in stud:
print(stud)

app = QApplication(sys.argv)
window = stafflogin()
window.show()

app.exec()

