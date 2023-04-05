import sqlite3
from sqlite3 import Connection
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget, QLineEdit, QHBoxLayout, QComboBox, QMessageBox

conn: Connection = sqlite3.connect('Main.db')


class staffupdate(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Staff Update")
        mainText = QLabel("Update Staff")
        mainText.setAlignment(Qt.AlignCenter)

        staffid = QLabel("Staff ID: ")
        self.staffidinput = QComboBox()
        self.staffidinput.addItem(" ")

        # Grabs the IDs from the staff table as String
        cursor = conn.execute("SELECT CAST(id AS TEXT) FROM Registration")
        staff = cursor.fetchall()
        for row in staff:
            self.staffidinput.addItems(row)

        # Performs the given function whenever the input value gets changed
        self.staffidinput.currentIndexChanged.connect(self.details)

        name = QLabel("Name: ")
        self.Nameinput = QLineEdit()

        DOB = QLabel("Date of Birth: ")
        self.DOBinput = QLineEdit()
        self.DOBinput.setInputMask("0000-00-00")

        Occupation = QLabel("Occupation: ")
        self.Occupationinput = QComboBox()
        self.Occupationinput.addItem("Software Engineer")
        self.Occupationinput.addItem("Clerk")

        username = QLabel("Username: ")
        self.usernameinput = QLineEdit()

        password = QLabel("Password: ")
        self.passwordinput = QLineEdit()
        self.passwordinput.setEchoMode(QLineEdit.Password)

        Updatebutton = QPushButton("Update")
        Updatebutton.clicked.connect(self.updatebutton)
        clearbtn = QPushButton("Clear")
        clearbtn.clicked.connect(self.clear)

        h_layout = QHBoxLayout()
        h_layout.addWidget(staffid)
        h_layout.addWidget(self.staffidinput)

        h_layout1 = QHBoxLayout()
        h_layout1.addWidget(name)
        h_layout1.addWidget(self.Nameinput)

        h_layout2 = QHBoxLayout()
        h_layout2.addWidget(DOB)
        h_layout2.addWidget(self.DOBinput)

        h_layout3 = QHBoxLayout()
        h_layout3.addWidget(Occupation)
        h_layout3.addWidget(self.Occupationinput)

        h_layout4 = QHBoxLayout()
        h_layout4.addWidget(username)
        h_layout4.addWidget(self.usernameinput)

        h_layout5 = QHBoxLayout()
        h_layout5.addWidget(password)
        h_layout5.addWidget(self.passwordinput)

        h_layout6 = QHBoxLayout()
        h_layout6.addWidget(Updatebutton)
        h_layout6.addWidget(clearbtn)

        v_layout = QVBoxLayout()
        v_layout.addWidget(mainText)
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        v_layout.addLayout(h_layout3)
        v_layout.addLayout(h_layout4)
        v_layout.addLayout(h_layout5)
        v_layout.addLayout(h_layout6)

        self.setLayout(v_layout)

    def clear(self):
        self.Nameinput.clear()
        self.DOBinput.clear()
        self.usernameinput.clear()
        self.passwordinput.clear()

    # Updates the Registration tables with the inputs given.
    def updatebutton(self):
        try:
            if len(self.Nameinput.text()) == 0 or len(self.DOBinput.text()) <= 5 or len(self.usernameinput.text()) == 0 or len(self.passwordinput.text()) == 0:
                message = QMessageBox()
                message.setMinimumSize(900, 200)
                message.setWindowTitle("Empty Fields")
                message.setText("All the fields have to be filled!")
                message.setIcon(QMessageBox.Critical)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()

            elif len(self.usernameinput.text()) <= 6 or len(self.passwordinput.text()) <= 6:
                message = QMessageBox()
                message.setMinimumSize(900, 200)
                message.setWindowTitle("Invalid Registration")
                message.setText("User name and Password have to be more than 6 characters!")
                message.setIcon(QMessageBox.Critical)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()

            else:
                conn.execute(
                    "UPDATE Registration SET name = ?,DOB = ?,occupation = ?,username = ?,password = ? WHERE id = ?",
                    [self.Nameinput.text(), self.DOBinput.text(), self.Occupationinput.currentText(),
                     self.usernameinput.text(), self.passwordinput.text(), self.staffidinput.currentText()])
                conn.commit()

                message = QMessageBox()
                message.setMinimumSize(900, 200)
                message.setWindowTitle("Staff Member Updated Successfully")
                message.setText("The member has been updated!")
                message.setIcon(QMessageBox.Information)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec()
        except:
            message = QMessageBox()
            message.setMinimumSize(900, 200)
            message.setWindowTitle("Error occurred")
            message.setText("An error has occurred. Please try again later.")
            message.setIcon(QMessageBox.Critical)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()


    def details(self):
        # Once the Staff ID is selected, the function will grab the details of the staff member and copy in the inputs
        if not self.staffidinput == " ":
            cursor = conn.execute("SELECT * FROM Registration WHERE id=?", [self.staffidinput.currentText()])
            info = cursor.fetchall()

            self.Nameinput.setText(info[0][1])
            self.DOBinput.setText(info[0][2])
            self.Occupationinput.setCurrentText(info[0][3])
            self.usernameinput.setText(info[0][4])
            self.passwordinput.setText(info[0][5])

