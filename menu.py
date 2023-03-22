from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox


class menu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")

        addStudentbtn = QPushButton("Add a Student")
        addStudentbtn.clicked.connect(self.addStudent)

        removeStudentbtn = QPushButton("Remove a Student")
        removeStudentbtn.clicked.connect(self.removeStudent)

        showStudentbtn = QPushButton("Show Student Details")
        showStudentbtn.clicked.connect(self.showStudent)

        showStaffbtn = QPushButton("Show Staff Details")
        showStaffbtn.clicked.connect(self.showStaff)

        layout = QVBoxLayout()
        layout.addWidget(addStudentbtn)
        layout.addWidget(removeStudentbtn)
        layout.addWidget(showStudentbtn)
        layout.addWidget(showStaffbtn)

        self.setLayout(layout)

    def addStudent(self):
        print("test")

    def removeStudent(self):
        print("test")

    def showStudent(self):
        print("test")

    def showStaff(self):
        print("test")




