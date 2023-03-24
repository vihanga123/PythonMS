import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox

conn: Connection = sqlite3.connect('Main.db')


class studentremove(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remove a Student")

        mainText = QLabel("Remove a Student")
        mainText.setAlignment(Qt.AlignCenter)

        selectStudent = QLabel("Select Student ID: ")
        self.selectStudentInput = QComboBox()
        cursor = conn.execute("SELECT CAST(id AS TEXT) FROM Student")
        users = cursor.fetchall()

        for row in users:
            self.selectStudentInput.addItems(row)


        removebtn = QPushButton("Remove")
        removebtn.clicked.connect(self.remove)

        showdetailsbtn = QPushButton("Show Details")
        showdetailsbtn.clicked.connect(self.showdetails)

        H_layout = QHBoxLayout()
        H_layout.addWidget(selectStudent)
        H_layout.addWidget(self.selectStudentInput)

        H_layout2 = QHBoxLayout()
        H_layout2.addWidget(removebtn)
        H_layout2.addWidget(showdetailsbtn)

        V_layout = QVBoxLayout()
        V_layout.addWidget(mainText)
        V_layout.addLayout(H_layout)
        V_layout.addLayout(H_layout2)

        self.setLayout(V_layout)


    def remove(self):
        print("Test")

    def showdetails(self):
        print("Test")
