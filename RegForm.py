import sys
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout


class register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Staff Registration")
        mainText = QLabel("Register")
        mainText.setAlignment(Qt.AlignCenter)

        name = QLabel("Name: ")
        Nameinput = QLineEdit()

        DOB = QLabel("Date of Birth: ")
        DOBinput = QLineEdit()
        DOBinput.setInputMask("0000-00-00")

        Occupation = QLabel("Occupation: ")
        Occupationinput = QLineEdit()

        username = QLabel("Username: ")
        usernameinput = QLineEdit()

        password = QLabel("Password: ")
        passwordinput = QLineEdit()
        passwordinput.setEchoMode(QLineEdit.Password)

        Regbutton = QPushButton("Register")
        clear = QPushButton("Clear")

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name)
        h_layout1.addWidget(Nameinput)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(DOB)
        h_layout2.addWidget(DOBinput)

        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(Occupation)
        h_layout3.addWidget(Occupationinput)

        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(username)
        h_layout4.addWidget(usernameinput)

        h_layout5 = QHBoxLayout()
        h_layout5.addWidget(password)
        h_layout5.addWidget(passwordinput)

        h_layout6 = QHBoxLayout()
        h_layout6.addWidget(Regbutton)
        h_layout6.addWidget(clear)

        v_layout = QVBoxLayout()
        v_layout.addWidget(mainText)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addLayout(h_layout5)
        v_layout.addLayout(h_layout6)

        self.setLayout(v_layout)
