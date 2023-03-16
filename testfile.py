import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QSlider, QWidget, QPushButton, QVBoxLayout, QMainWindow, QToolBar, QStatusBar

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
        
"""



"""
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Title")

        # Menubar and menus
        menu = self.menuBar()
        file_menu = menu.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit)

        about_menu = menu.addMenu("About")
        license_action = about_menu.addAction("License")
        about = about_menu.addAction("About")
        # about.triggered.connect(self.about)

        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("Test action", self)
        action1.setStatusTip("Status messege of actions")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("image.png"),"New Action", self)
        action2.setStatusTip("Status message")
        action2.triggered.connect(self.toolbar_icon)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("CLick here"))

        #Status bar
        self.setStatusBar(QStatusBar(self))

        #Button
        button1 = QPushButton("Button")
        button1.clicked.connect(self.button)
        self.setCentralWidget(button1)

    def quit(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("This is the message shown by the status bar", 3000)

    def toolbar_icon(self):
        print("Image will be shown")

    def button(self):
        print("The button has been pressed")
        self.statusBar().showMessage("The button has been pressed",1000)
"""


