from PySide6.QtWidgets import QMainWindow, QPushButton


class NewButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("This is a Button")
        button = QPushButton("Press")

        self.setCentralWidget(button)
