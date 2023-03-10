


"""
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        button = QPushButton("Press")
        self.setCentralWidget(button)

"""
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QPushButton
from NewButton import NewButton


app = QApplication(sys.argv)
window = NewButton()
window.show()
app.exec()


