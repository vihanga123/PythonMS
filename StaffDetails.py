import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox, QTableWidget
from PySide6 import QtWidgets

conn: Connection = sqlite3.connect('Main.db')


class staffdetails(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Staff Details Viewer")
        maintext = QLabel("Staff Details")
        maintext.setAlignment(Qt.AlignCenter)

        cursor = conn.execute("SELECT id FROM Registration ORDER BY id DESC LIMIT 1;")
        info = cursor.fetchone()
        cursor2 = conn.execute("SELECT * FROM Registration")
        staff = cursor2.fetchall()

        self.table = QTableWidget((info[0]) + 1, 4)

        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("ID"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Name"))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem("Date of Birth"))
        self.table.setItem(0, 3, QtWidgets.QTableWidgetItem("Occupation"))

        s = 1

        while s <= info[0]:
            t = 0
            while t <= 3:
                self.table.setItem(s, t, QtWidgets.QTableWidgetItem(str(staff[s - 1][t])))
                t += 1
            s += 1

        Layout = QVBoxLayout()
        Layout.addWidget(maintext)
        Layout.addWidget(self.table)

        self.setLayout(Layout)
