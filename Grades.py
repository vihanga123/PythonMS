import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QHBoxLayout, QComboBox, QMessageBox, QLineEdit, QApplication

conn: Connection = sqlite3.connect('Main.db')


class grades(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Grades")
        maintitle = QLabel("Add Student Grades")
        maintitle.setAlignment(Qt.AlignCenter)

        studentid = QLabel("Select User ID: ")
        self.studentidinput = QComboBox()
        self.studentidinput.addItem(" ")

        cursor = conn.execute("SELECT CAST(id AS TEXT) FROM Student")
        students = cursor.fetchall()

        for row in students:
            self.studentidinput.addItems(row)

        self.studentidinput.currentIndexChanged.connect(self.studentdetails)

        #self.studentidinput.currentIndexChanged.connect(self.details)

        self.studentinfo = QLabel()

        self.subject1 = QLabel()
        self.subject1.setFixedSize(150, 20)
        self.subject1input = QLineEdit()
        self.subject1input.setInputMask("###")
        self.subject1input.setFixedSize(30, 20)

        self.subject2 = QLabel()
        self.subject2.setFixedSize(150, 20)
        self.subject2input = QLineEdit()
        self.subject2input.setInputMask("###")
        self.subject2input.setFixedSize(30, 20)

        self.subject3 = QLabel()
        self.subject3.setFixedSize(150, 20)
        self.subject3input = QLineEdit()
        self.subject3input.setInputMask("###")
        self.subject3input.setFixedSize(30, 20)

        addgradesbtn = QPushButton("Add Grades")
        addgradesbtn.clicked.connect(self.addgrades)

        H_layout = QHBoxLayout()
        H_layout.addWidget(studentid)
        H_layout.addWidget(self.studentidinput)

        H_layout1 = QHBoxLayout()
        H_layout1.addWidget(self.subject1)
        H_layout1.addWidget(self.subject1input)
        H_layout2 = QHBoxLayout()
        H_layout2.addWidget(self.subject2)
        H_layout2.addWidget(self.subject2input)
        H_layout3 = QHBoxLayout()
        H_layout3.addWidget(self.subject3)
        H_layout3.addWidget(self.subject3input)


        V_Layout = QVBoxLayout()
        V_Layout.addWidget(maintitle)
        V_Layout.addLayout(H_layout)
        V_Layout.addWidget(self.studentinfo)
        V_Layout.addLayout(H_layout1)
        V_Layout.addLayout(H_layout2)
        V_Layout.addLayout(H_layout3)
        V_Layout.addWidget(addgradesbtn)

        self.setLayout(V_Layout)

    def addgrades(self):
        maincursor = conn.execute("SELECT subject FROM Student WHERE id=?", [self.studentidinput.currentText()])
        sub = maincursor.fetchone()[0]
        cursor = conn.execute("SELECT id FROM SubjectModule WHERE module=?", [self.subject1.text()])
        mod1 = cursor.fetchone()[0]
        cursor1 = conn.execute("SELECT id FROM SubjectModule WHERE module=?", [self.subject2.text()])
        mod2 = cursor1.fetchone()[0]
        cursor2 = conn.execute("SELECT id FROM SubjectModule WHERE module=?", [self.subject3.text()])
        mod3 = cursor2.fetchone()[0]

        conn.execute("INSERT INTO StudentGrade (sid,mid,subject,grade) VALUES (?, ?, ?, ?)",
                     [self.studentidinput.currentText(), mod1, sub, self.subject1input.text()])
        conn.execute("INSERT INTO StudentGrade (sid,mid,subject,grade) VALUES (?, ?, ?, ?)",
                     [self.studentidinput.currentText(), mod2, sub, self.subject2input.text()])
        conn.execute("INSERT INTO StudentGrade (sid,mid,subject,grade) VALUES (?, ?, ?, ?)",
                     [self.studentidinput.currentText(), mod3, sub, self.subject3input.text()])
        conn.commit()

        message = QMessageBox()
        message.setMinimumSize(900, 200)
        message.setWindowTitle("Student Grades are stored")
        message.setText("The student grades have been stored!")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec()

    def studentdetails(self):
        cursor = conn.execute("SELECT * FROM Student WHERE id=?", [self.studentidinput.currentText()])
        info = cursor.fetchone()
        self.studentinfo.setText("ID: " + str(info[0]) + "\n" +
                                "Name: " + str(info[1]) + "\n" +
                                "Subject: " + str(info[5]) + "\n")

        cursor = conn.execute("SELECT subject FROM Student WHERE id=?", [self.studentidinput.currentText()])
        select = cursor.fetchone()[0]
        if select == "Software Engineering":
            self.subject1.setText("Mathematics")
            self.subject2.setText("OOP")
            self.subject3.setText("Database Management")
        elif select == "Network Engineering":
            self.subject1.setText("Data Communication")
            self.subject2.setText("Database Management")
            self.subject3.setText("Routing and Switching")
        else:
            self.subject1.setText("GUI Design")
            self.subject2.setText("Mobile App Development")
            self.subject3.setText("Computer Technology")