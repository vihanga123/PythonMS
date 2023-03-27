import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QComboBox, QMessageBox

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

        H_layout = QHBoxLayout()
        H_layout.addWidget(studentid)
        H_layout.addWidget(self.studentidinput)

        V_Layout = QVBoxLayout()
        V_Layout.addWidget(maintitle)
        V_Layout.addLayout(H_layout)
        V_Layout.addWidget(addgradesbtn)

        self.setLayout(V_Layout)

