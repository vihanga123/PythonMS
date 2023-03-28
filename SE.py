import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox, QMessageBox

conn: Connection = sqlite3.connect('Main.db')


class SoftwareEngineering(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Submit Grades")

        mainText = QLabel("Submit Student Grades")
        mainText.setAlignment(Qt.AlignCenter)

        mathematics = QLabel("Mathematics: ")
        self.mathematicsinput = QLineEdit()

        oop = QLabel("OOP: ")
        self.oopinput = QLineEdit()

        dbm = QLabel("Database Management: ")
        self.dbminput = QLineEdit()

        submitbtn = QPushButton("Submit")
        submitbtn.clicked.connect(self.submit)

        clearbtn = QPushButton("Clear")
        clearbtn.clicked.connect(self.clear)

        H_layout1 = QHBoxLayout()
        H_layout1.addWidget(mathematics)
        H_layout1.addWidget(self.mathematicsinput)

        H_layout2 = QHBoxLayout()
        H_layout2.addWidget(oop)
        H_layout2.addWidget(self.oopinput)

        H_layout3 = QHBoxLayout()
        H_layout3.addWidget(dbm)
        H_layout3.addWidget(self.dbminput)

        H_layout4 = QHBoxLayout()
        H_layout4.addWidget(submitbtn)
        H_layout4.addWidget(clearbtn)

        V_layout = QVBoxLayout()
        V_layout.addWidget(mainText)
        V_layout.addLayout(H_layout1)
        V_layout.addLayout(H_layout2)
        V_layout.addLayout(H_layout3)
        V_layout.addLayout(H_layout4)

        self.setLayout(V_layout)

    def submit(self):
        print("test")

    def clear(self):
        print("test")

