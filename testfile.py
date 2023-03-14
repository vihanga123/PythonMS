import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider, QWidget, QPushButton,QVBoxLayout

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
        button2 = QPushButton("Button 2")

        button1.clicked.connect(self.button_message)
        button2.clicked.connect(self.button_message)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)


        self.setLayout(button_layout)

    def button_message(self):
        print("Button Pressed")