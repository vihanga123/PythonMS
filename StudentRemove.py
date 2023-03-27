import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QComboBox, QMessageBox

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
        conn.execute("DELETE FROM Student WHERE id=? ",
                     [self.selectStudentInput.currentText()])
        conn.commit()

        message = QMessageBox()
        message.setMinimumSize(900, 200)
        message.setWindowTitle("The Student has been Removed Successfully")
        message.setText("The student has been removed from the database!")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()

        self.selectStudentInput.clear()

        cursor = conn.execute("SELECT CAST(id AS TEXT) FROM Student")
        users = cursor.fetchall()

        for row in users:
            self.selectStudentInput.addItems(row)

    def showdetails(self):
        cursor = conn.execute("SELECT * FROM Student WHERE id=?", [self.selectStudentInput.currentText()])
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
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()
