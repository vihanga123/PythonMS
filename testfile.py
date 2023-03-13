import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider, QWidget, QPushButton,QHBoxLayout

"""
def button_clicked(data):
    print("You have clicked the button",data)


app = QApplication()

button = QPushButton("Press this")
button.setCheckable(True)
button.clicked.connect(button_clicked)

button.show()
app.exec()

"""
"""def slider(data):
    print ("Slider have moved to",data)

app = QApplication()
sd=QSlider(Qt.Horizontal)
sd.setMinimum(1)
sd.setMaximum(100)
sd.setValue(20)

sd.valueChanged.connect(slider)
sd.show()
app.exec()
"""


class widget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widgets")
        button1 = QPushButton("Button1")

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)

        self.setLayout(button_layout)
