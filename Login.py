import sqlite3
import sys
from sqlite3 import Connection
from RegForm import register
from menu import menu
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QMessageBox

conn: Connection = sqlite3.connect('Main.db')


class stafflogin(QWidget):
    def __init__(self):
        super().__init__()
        self.window = None
        self.setWindowTitle("Staff Login")
        self.setWindowFlag(Qt.WindowType.WindowDoesNotAcceptFocus)
        mainText = QLabel("Loginr")
        mainText.setAlignment(Qt.AlignCenter)

        username = QLabel("Username: ")
        self.usernameInput = QLineEdit()

        password = QLabel("Password: ")
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)

        login = QPushButton("Login")
        login.clicked.connect(self.loginclicked)

        register = QPushButton("Register")
        register.clicked.connect(self.registerclicked)

        clear = QPushButton("Clear")
        clear.clicked.connect(self.clearclicked)

        h_layout = QHBoxLayout()
        h_layout.addWidget(username)
        h_layout.addWidget(self.usernameInput)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(password)
        h_layout2.addWidget(self.passwordInput)

        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(login)
        h_layout3.addWidget(clear)
        h_layout3.addWidget(register)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)

        self.setLayout(v_layout)

    def loginclicked(self):
        cursor = conn.execute("SELECT username,password FROM Registration WHERE username=? AND password=? ", [self.usernameInput.text(), self.passwordInput.text()])
        users = cursor.fetchone()

        if users is not None and users[0] == self.usernameInput.text():
            if users is not None and users[1] == self.passwordInput.text():
                print("Login Successful")
                self.window = menu()
                self.window.show()

        else:
            message = QMessageBox()
            message.setMinimumSize(900, 200)
            message.setWindowTitle("Wrong Username or Password")
            message.setText("The given Username or the Password is incorrect!")
            message.setIcon(QMessageBox.Critical)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()

    def clearclicked(self):
        self.usernameInput.clear()
        self.passwordInput.clear()

    def registerclicked(self):
        self.window = register()
        self.window.show()


