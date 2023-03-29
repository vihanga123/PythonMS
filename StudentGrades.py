import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QComboBox, QMessageBox

conn: Connection = sqlite3.connect('Main.db')


class studentgrades(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Student Grades")
        maintitle = QLabel("Student Grades")
        maintitle.setAlignment(Qt.AlignCenter)

        studentid = QLabel("Select User ID: ")
        self.studentidinput = QComboBox()
        self.studentidinput.addItem(" ")

        cursor = conn.execute("SELECT CAST(id AS TEXT) FROM Student")
        students = cursor.fetchall()

        for row in students:
            self.studentidinput.addItems(row)

        self.studentidinput.currentIndexChanged.connect(self.studentgrades)

        self.info = QLabel()

        H_layout = QHBoxLayout()
        H_layout.addWidget(studentid)
        H_layout.addWidget(self.studentidinput)

        V_layout = QVBoxLayout()
        V_layout.addWidget(maintitle)
        V_layout.addLayout(H_layout)
        V_layout.addWidget(self.info)


        self.setLayout(V_layout)

    def studentgrades(self):
        try:
            maincursor = conn.execute("SELECT name,subject FROM Student WHERE id=?",
                                      [self.studentidinput.currentText()])
            sub = maincursor.fetchone()

            cursor = conn.execute("SELECT module FROM SubjectModule WHERE subject=?", [sub[1]])
            mod = cursor.fetchall()

            cursor2 = conn.execute("SELECT grade FROM StudentGrade WHERE sid=?", [self.studentidinput.currentText()])
            grade = cursor2.fetchall()

            self.info.setText("Name: " + str(sub[0]) + "\n" +
                              "Subject: " + str(sub[1]) + "\n" +
                              str(mod[0]) + " " + str(grade[0]) + "\n" +
                              str(mod[1]) + " " + str(grade[1]) + "\n" +
                              str(mod[2]) + " " + str(grade[2]) + "\n")

        except:
            message = QMessageBox()
            message.setMinimumSize(900, 200)
            message.setWindowTitle("No Grades found")
            message.setText("This Student's Grades have not been added yet!")
            message.setIcon(QMessageBox.Critical)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()
