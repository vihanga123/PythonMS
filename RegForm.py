
import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox

conn: Connection = sqlite3.connect('Main.db')


class register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Staff Registration")
        mainText = QLabel("Register")
        mainText.setAlignment(Qt.AlignCenter)

        name = QLabel("Name: ")
        self.Nameinput = QLineEdit()

        DOB = QLabel("Date of Birth: ")
        self.DOBinput = QLineEdit()
        self.DOBinput.setInputMask("0000-00-00")

        Occupation = QLabel("Occupation: ")
        self.Occupationinput = QComboBox()
        self.Occupationinput.addItem("Software Engineer")
        self.Occupationinput.addItem("Clerk")

        username = QLabel("Username: ")
        self.usernameinput = QLineEdit()

        password = QLabel("Password: ")
        self.passwordinput = QLineEdit()
        self.passwordinput.setEchoMode(QLineEdit.Password)

        Regbutton = QPushButton("Register")
        Regbutton.clicked.connect(self.regbutton)
        clearbtn = QPushButton("Clear")
        clearbtn.clicked.connect(self.clear)

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name)
        h_layout1.addWidget(self.Nameinput)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(DOB)
        h_layout2.addWidget(self.DOBinput)

        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(Occupation)
        h_layout3.addWidget(self.Occupationinput)

        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(username)
        h_layout4.addWidget(self.usernameinput)

        h_layout5 = QHBoxLayout()
        h_layout5.addWidget(password)
        h_layout5.addWidget(self.passwordinput)

        h_layout6 = QHBoxLayout()
        h_layout6.addWidget(Regbutton)
        h_layout6.addWidget(clearbtn)

        v_layout = QVBoxLayout()
        v_layout.addWidget(mainText)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addLayout(h_layout5)
        v_layout.addLayout(h_layout6)

        self.setLayout(v_layout)

    def clear(self):
        self.Nameinput.clear()
        self.DOBinput.clear()
        self.usernameinput.clear()
        self.passwordinput.clear()

    def regbutton(self):
        conn.execute("INSERT INTO Registration (name,DOB,occupation,username,password) VALUES (?, ?, ?, ?, ?)",
                     [self.usernameinput.text(), self.DOBinput.text(), self.Occupationinput.currentText(),
                      self.usernameinput.text(), self.passwordinput.text()])
        conn.commit()
        print("Staff Registered Successfully")



