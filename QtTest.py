import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        button = QPushButton("Press")
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
