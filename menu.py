from PySide6.QtWidgets import QVBoxLayout, QPushButton, QWidget

from StudentReg import studentReg
from StudentRemove import studentremove
from StudentDetails import studentdetails
from StaffDetails import staffdetails
from StaffUpdate import staffupdate
from StudentUpdate import studentupdate
from Grades import grades
from StudentGrades import studentgrades


class menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")

        addStudentbtn = QPushButton("Add a Student")
        addStudentbtn.clicked.connect(self.addStudent)

        addGradesbtn = QPushButton("Add Student Grades")
        addGradesbtn.clicked.connect(self.addGrades)

        viewGradesbtn = QPushButton("View Student Grades")
        viewGradesbtn.clicked.connect(self.viewGrades)

        removeStudentbtn = QPushButton("Remove a Student")
        removeStudentbtn.clicked.connect(self.removeStudent)

        showStudentbtn = QPushButton("Show Student Details")
        showStudentbtn.clicked.connect(self.showStudent)

        showStaffbtn = QPushButton("Show Staff Details")
        showStaffbtn.clicked.connect(self.showStaff)

        updateStaffbtn = QPushButton("Update Staff Details")
        updateStaffbtn.clicked.connect(self.updateStaff)

        updateStudentbtn = QPushButton("Update Student Details")
        updateStudentbtn.clicked.connect(self.updateStudent)

        layout = QVBoxLayout()
        layout.addWidget(addStudentbtn)
        layout.addWidget(addGradesbtn)
        layout.addWidget(viewGradesbtn)
        layout.addWidget(removeStudentbtn)
        layout.addWidget(showStudentbtn)
        layout.addWidget(showStaffbtn)
        layout.addWidget(updateStaffbtn)
        layout.addWidget(updateStudentbtn)

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
        self.window = grades()
        self.window.show()

    def viewGrades(self):
        self.window = studentgrades()
        self.window.show()

    def updateStaff(self):
        self.window = staffupdate()
        self.window.show()

    def updateStudent(self):
        self.window = studentupdate()
        self.window.show()





