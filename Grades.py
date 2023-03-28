import sqlite3
import sys
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QComboBox, QMessageBox, QLineEdit, QApplication

from AD import ApplicationDevelopment
from SE import SoftwareEngineering
from NE import NetworkEngineering
conn: Connection = sqlite3.connect('Main.db')


class studentgrades(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grades")
        maintitle = QLabel("Add Student Grades")
        maintitle.setAlignment(Qt.AlignCenter)

        studentid = QLabel("Select User ID: ")
        self.studentidinput = QComboBox()

        cursor = conn.execute("SELECT CAST(id AS TEXT) FROM Student")
        students = cursor.fetchall()

        for row in students:
            self.studentidinput.addItems(row)

        #self.studentidinput.currentIndexChanged.connect(self.details)

        addgradesbtn = QPushButton("Add Grades")
        addgradesbtn.clicked.connect(self.addgrades)

        H_layout = QHBoxLayout()
        H_layout.addWidget(studentid)
        H_layout.addWidget(self.studentidinput)

        V_Layout = QVBoxLayout()
        V_Layout.addWidget(maintitle)
        V_Layout.addLayout(H_layout)
        V_Layout.addWidget(addgradesbtn)

        self.setLayout(V_Layout)

    def addgrades(self):
        cursor = conn.execute("SELECT * FROM Student WHERE id=?", [self.studentidinput.currentText()])
        info = cursor.fetchone()
        message = QMessageBox()
        message.setMinimumSize(900, 200)
        message.setWindowTitle("Student Information")
        message.setText("ID: " + str(info[0]) + "\n" +
                        "Name: " + str(info[1]) + "\n" +
                        "Age: " + str(info[2]) + "\n" +
                        "Address: " + str(info[3]) + "\n" +
                        "Telephone: " + str(info[4]) + "\n" +
                        "Subject: " + str(info[5]) + "\n")

        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        ok = message.button(QMessageBox.Ok)
        ok.setText("Add Grades")
        ret = message.exec()
        if ret == QMessageBox.Ok:
            cursor = conn.execute("SELECT subject FROM Student WHERE id=?", [self.studentidinput.currentText()])
            select = cursor.fetchone()[0]
            if select == "Software Engineering":
                self.Soften()
            elif select == "Network Engineering":
                self.Neten()
            else:
                self.Appdev()


    def Soften(self):
        self.window = SoftwareEngineering()
        self.window.show()
    def Neten(self):
        self.window = NetworkEngineering()
        self.window.show()
    def Appdev(self):
        self.window = ApplicationDevelopment()
        self.window.show()


