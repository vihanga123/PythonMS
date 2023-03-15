


"""
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        button = QPushButton("Press")
        self.setCentralWidget(button)

"""
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QPushButton, QWidget
from testfile import MainWindow


app = QApplication(sys.argv)
window = MainWindow(app)
window.show()

app.exec()


