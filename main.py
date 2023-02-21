import tkinter
import sqlite3
from tkinter import *

conn = sqlite3.connect('test.db')
c = conn.cursor()
#table
def initialize_table():

c.execute('''CREATE TABLE IF NOT EXISTS user(username text,password text)''')
c.execute("INSERT INTO user VALUES('vihanga','test')")
messagebox.showinfo("Success", "User added successfully!")
c.execute ("SELECT * FROM user WHERE username=?",(test))
rows = c.fetchall()
for row in rows:
    print(row)

print (test)

def get_user():
    username= user.get()
    pw=password.get()

    c.execute("SELECT * FROM user WHERE username=? AND password=?", (username, pw))
    check = c.fetchone()
    if check is not None:
        print("Success")
    else:
        print("Invalid")

def combine():
    initialize_table()
    get_user()
    conn.commit()

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

button = tkinter.Button(text="Input",command= combine)
button.grid(row=5,column=1)
button2 = tkinter.Button(text='clear',command=clear)
button2.grid(row=5,column=2)



top.mainloop()
conn.close()