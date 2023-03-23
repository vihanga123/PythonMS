import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox

conn: Connection = sqlite3.connect('Main.db')

class studentReg(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register a Student")

        mainText = QLabel("Student Registrationr")
        mainText.setAlignment(Qt.AlignCenter)

        name = QLabel("Student Name: ")
        self.nameinput = QLineEdit()

        age = QLabel("Student Age: ")
        self.ageinput = QLineEdit()

        address = QLabel("Address: ")
        self.addressinput = QLineEdit()

        telephone = QLabel("Telephone: ")
        self.telephoneinput = QLineEdit()
        self.telephoneinput.setInputMask("##########")

        registerbtn = QPushButton("Register Student")
        registerbtn.clicked.connect(self.register)

        clearbtn = QPushButton("Clear")
        clearbtn.clicked.connect(self.clear)

        H_layout = QHBoxLayout()
        H_layout.addWidget(name)
        H_layout.addWidget(self.nameinput)

        H_layout2 = QHBoxLayout()
        H_layout2.addWidget(age)
        H_layout2.addWidget(self.ageinput)

        H_layout3 = QHBoxLayout()
        H_layout3.addWidget(address)
        H_layout3.addWidget(self.addressinput)

        H_layout4 = QHBoxLayout()
        H_layout4.addWidget(telephone)
        H_layout4.addWidget(self.telephoneinput)

        H_layout5 = QHBoxLayout()
        H_layout5.addWidget(registerbtn)
        H_layout5.addWidget(clearbtn)

        V_layout = QVBoxLayout()
        V_layout.addWidget(mainText)
        V_layout.addLayout(H_layout)
        V_layout.addLayout(H_layout2)
        V_layout.addLayout(H_layout3)
        V_layout.addLayout(H_layout4)
        V_layout.addLayout(H_layout5)

        self.setLayout(V_layout)

    def register(self):
        print("test")

    def clear(self):
        self.nameinput.clear()
        self.ageinput.clear()
        self.addressinput.clear()
        self.telephoneinput.clear()
