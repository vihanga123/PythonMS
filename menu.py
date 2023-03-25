from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox

from StudentReg import studentReg
from StudentRemove import studentremove
from StudentDetails import studentdetails
from StaffDetails import staffdetails


class menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")

        addStudentbtn = QPushButton("Add a Student")
        addStudentbtn.clicked.connect(self.addStudent)

        addGradesbtn = QPushButton("Add Student Grades")
        addGradesbtn.clicked.connect(self.addGrades)

        removeStudentbtn = QPushButton("Remove a Student")
        removeStudentbtn.clicked.connect(self.removeStudent)

        showStudentbtn = QPushButton("Show Student Details")
        showStudentbtn.clicked.connect(self.showStudent)

        showStaffbtn = QPushButton("Show Staff Details")
        showStaffbtn.clicked.connect(self.showStaff)

        layout = QVBoxLayout()
        layout.addWidget(addStudentbtn)
        layout.addWidget(addGradesbtn)
        layout.addWidget(removeStudentbtn)
        layout.addWidget(showStudentbtn)
        layout.addWidget(showStaffbtn)

        self.setLayout(layout)

    def addStudent(self):
        self.window = studentReg()
        self.window.show()

    def removeStudent(self):
        self.window = studentremove()
        self.window.show()

    def showStudent(self):
        self.window = studentdetails()
        self.window.show()

    def showStaff(self):
        self.window = staffdetails()
        self.window.show()

    def addGrades(self):
        print("test")




