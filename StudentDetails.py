import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QWidget, QTableWidget
from PySide6 import QtWidgets

conn: Connection = sqlite3.connect('Main.db')


class studentdetails(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Details Viewer")
        mainText = QLabel("Student Details")
        mainText.setAlignment(Qt.AlignCenter)

        #Grabs the count of the available rows in Student table
        cursor = conn.execute("SELECT count(*) FROM Student;")
        info = cursor.fetchone()
        cursor2 = conn.execute("SELECT * FROM Student")
        student = cursor2.fetchall()

        # Creates a Qt table with the given amount of columns and rows
        self.table = QTableWidget((info[0])+1,6)

        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("ID"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("Name"))
        self.table.setItem(0, 2, QtWidgets.QTableWidgetItem("Age"))
        self.table.setItem(0, 3, QtWidgets.QTableWidgetItem("Address"))
        self.table.setItem(0, 4, QtWidgets.QTableWidgetItem("Telephone"))
        self.table.setItem(0, 5, QtWidgets.QTableWidgetItem("Subject"))

        # Pulls data from the database and arrange them accordingly as given in the table
        s = 1
        while s <= info[0]:
            t = 0
            while t <= 5:
                self.table.setItem(s, t, QtWidgets.QTableWidgetItem(str(student[s-1][t])))
                t += 1
            s += 1

        Layout = QVBoxLayout()
        Layout.addWidget(mainText)
        Layout.addWidget(self.table)

        self.setLayout(Layout)
