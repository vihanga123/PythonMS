import tkinter
import sqlite3
from tkinter import *

#table


def clear():
    user.delete(0,tkinter.END)
    password.delete(0,tkinter.END)


top=Tk()
top.title("Student LMS")
#top.geometry("300x200")
heading = tkinter.Label(text="This is a test", background="#34A2FE",foreground="white")
heading.grid(row=0,column=2)

label=tkinter.Label(text="Insert Name: ")
label.grid(row=2,column=1)
user=tkinter.Entry()
user.grid(row=2,column=2)

label=tkinter.Label(text="Insert Password: ")
label.grid(row=4,column=1)
password=tkinter.Entry(show="*")
password.grid(row=4,column=2)


button2 = tkinter.Button(text='clear',command=clear)
button2.grid(row=5,column=2)

def login():
    conn = sqlite3.connect('test.db')
    print("test")

    conn.execute('''CREATE TABLE IF NOT EXISTS user(username text,password text)''')
    conn.execute("INSERT INTO user VALUES('vihanga','test')")
    conn.commit()
    print("Success", "User added successfully!")

    cursor = conn.execute("SELECT * FROM user")
    check = conn.cursor()
    if check is not None:
        print("Success")
    else:
        print("Invalid")


    username= user.get()
    pw=password.get()

    cursor = conn.execute("SELECT username FROM user")##WHERE username=?",username)
    users = cursor.fetchone()
    print (users)

    if users is not None and users[1]==pw:
        print("Success")
    else:
        print("Failure")

    conn.close()

button = tkinter.Button(text="Input",command= login)
button.grid(row=5,column=1)

top.mainloop()
