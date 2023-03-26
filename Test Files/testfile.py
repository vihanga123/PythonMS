import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QSlider, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow, QToolBar, QStatusBar, QLabel, QLineEdit

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

"""
def button_clicked(data):
    print("You have clicked the button",data)


app = QApplication()

button = QPushButton("Press this")
button.setCheckable(True)
button.clicked.connect(button_clicked)

button.show()
app.exec()

"""
"""def slider(data):
    print ("Slider have moved to",data)

app = QApplication()
sd=QSlider(Qt.Horizontal)
sd.setMinimum(1)
sd.setMaximum(100)
sd.setValue(20)

sd.valueChanged.connect(slider)
sd.show()
app.exec()
"""

"""
class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets")
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button 2")

        button1.clicked.connect(self.button_message)
        button2.clicked.connect(self.button_message)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)


        self.setLayout(button_layout)

    def button_message(self):
        print("Button Pressed")
        
"""



"""
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Title")

        # Menubar and menus
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)

        about_menu = menu.addMenu("About")
        license_action = about_menu.addAction("License")
        about = about_menu.addAction("About")
        # about.triggered.connect(self.about)

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Test action", self)
        action1.setStatusTip("Status messege of actions")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("image.png"),"New Action", self)
        action2.setStatusTip("Status message")
        action2.triggered.connect(self.toolbar_icon)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("CLick here"))

        #Status bar
        self.setStatusBar(QStatusBar(self))

        #Button
        button1 = QPushButton("Button")
        button1.clicked.connect(self.button)
        self.setCentralWidget(button1)

    def quit(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("This is the message shown by the status bar", 3000)

    def toolbar_icon(self):
        print("Image will be shown")

    def button(self):
        print("The button has been pressed")
        self.statusBar().showMessage("The button has been pressed",1000)
"""

"""
class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Push Button")
        button = QPushButton("Click here")
        button.clicked.connect(self.buttonclicked)
        button.pressed.connect(self.buttonpressed)
        button.released.connect(self.buttonreleased)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)

    def buttonclicked(self):
        print("Clicked")

    def buttonpressed(self):
        print("Pressed")

    def buttonreleased(self):
        print("released")
"""

class widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The title")
        label = QLabel("Enter Text: ")
        self.line_edit = QLineEdit()
        button = QPushButton("Click here")
        button.clicked.connect(self.buttonclicked)
        self.text_holder = QLabel("Configured")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder)

        self.setLayout(v_layout)

    def buttonclicked(self):
        print("The text is : ", self.line_edit.text())




