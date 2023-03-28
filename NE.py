import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox, QMessageBox

conn: Connection = sqlite3.connect('Main.db')


class NetworkEngineering(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Submit Grades")

        mainText = QLabel("Submit Student Grades")
        mainText.setAlignment(Qt.AlignCenter)

        datacom = QLabel("Data Communication: ")
        self.datacominput = QLineEdit()

        dbm = QLabel("Database Management: ")
        self.dbminput = QLineEdit()

        routing = QLabel("Routing and Switching: ")
        self.routinginput = QLineEdit()

        submitbtn = QPushButton("Submit")
        submitbtn.clicked.connect(self.submit)

        clearbtn = QPushButton("Clear")
        clearbtn.clicked.connect(self.clear)

        H_layout1 = QHBoxLayout()
        H_layout1.addWidget(datacom)
        H_layout1.addWidget(self.datacominput)

        H_layout2 = QHBoxLayout()
        H_layout2.addWidget(dbm)
        H_layout2.addWidget(self.dbminput)

        H_layout3 = QHBoxLayout()
        H_layout3.addWidget(routing)
        H_layout3.addWidget(self.routinginput)

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

