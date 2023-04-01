import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox, QMessageBox

conn: Connection = sqlite3.connect('Main.db')


class studentupdate(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student")

        mainText = QLabel("Update Student Details")
        mainText.setAlignment(Qt.AlignCenter)

        studentid = QLabel("Student ID: ")
        self.studentidinput = QComboBox()
        self.studentidinput.addItem(" ")

        # Takes the Student table IDs as String
        cursor = conn.execute("SELECT CAST(id AS TEXT) FROM Student")
        students = cursor.fetchall()

        for row in students:
            self.studentidinput.addItems(row)

        self.studentidinput.currentIndexChanged.connect(self.details)

        name = QLabel("Student Name: ")
        self.nameinput = QLineEdit()

        age = QLabel("Student Age: ")
        self.ageinput = QLineEdit()
        self.ageinput.setInputMask("##")

        address = QLabel("Address: ")
        self.addressinput = QLineEdit()

        telephone = QLabel("Telephone: ")
        self.telephoneinput = QLineEdit()
        self.telephoneinput.setInputMask("##########")

        course = QLabel("Subject: ")
        self.courseinput = QComboBox()
        self.courseinput.addItem("Software Engineering")
        self.courseinput.addItem("Network Engineering")
        self.courseinput.addItem("Application Development")

        registerbtn = QPushButton("Register Student")
        registerbtn.clicked.connect(self.register)

        clearbtn = QPushButton("Clear")
        clearbtn.clicked.connect(self.clear)

        H_layout = QHBoxLayout()
        H_layout.addWidget(studentid)
        H_layout.addWidget(self.studentidinput)

        H_layout1 = QHBoxLayout()
        H_layout1.addWidget(name)
        H_layout1.addWidget(self.nameinput)

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
        H_layout5.addWidget(course)
        H_layout5.addWidget(self.courseinput)

        H_layout6 = QHBoxLayout()
        H_layout6.addWidget(registerbtn)
        H_layout6.addWidget(clearbtn)

        V_layout = QVBoxLayout()
        V_layout.addWidget(mainText)
        V_layout.addLayout(H_layout)
        V_layout.addLayout(H_layout1)
        V_layout.addLayout(H_layout2)
        V_layout.addLayout(H_layout3)
        V_layout.addLayout(H_layout4)
        V_layout.addLayout(H_layout5)
        V_layout.addLayout(H_layout6)

        self.setLayout(V_layout)

    def register(self):
        # Updates the Student table accordingly with the taken user inputs
        conn.execute("Update Student SET name = ?,age = ?,address = ?,telephone = ?,subject = ? WHERE id = ?",
                     [self.nameinput.text(), self.ageinput.text(), self.addressinput.text(),
                      self.telephoneinput.text(), self.courseinput.currentText(), self.studentidinput.currentText()])
        conn.commit()

        message = QMessageBox()
        message.setMinimumSize(900, 200)
        message.setWindowTitle("Student has been Updated")
        message.setText("The student record has been updated successfully")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()

    def clear(self):
        self.nameinput.clear()
        self.ageinput.clear()
        self.addressinput.clear()
        self.telephoneinput.clear()

    def details(self):
        # Once the Student ID is selected, the function will grab the details of the staff member and copy in the inputs
        if not self.studentidinput == " ":
            cursor = conn.execute("SELECT * FROM Student WHERE id=?", [self.studentidinput.currentText()])
            info = cursor.fetchall()

            self.nameinput.setText(info[0][1])
            self.ageinput.setText(str(info[0][2]))
            self.addressinput.setText(info[0][3])
            self.telephoneinput.setText(str(info[0][4]))
            self.courseinput.setCurrentText(info[0][5])
