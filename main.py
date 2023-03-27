import sys
import sqlite3
from sqlite3 import Connection
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QPushButton, QWidget
from Login import stafflogin

conn: Connection = sqlite3.connect('Main.db')

conn.execute("CREATE TABLE IF NOT EXISTS Registration (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,DOB DATE,occupation TEXT,username TEXT,password TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,address TEXT,telephone INTEGER,subject TEXT, FOREIGN KEY(subject) REFERENCES Subject(subject))")
#conn.execute("DROP TABLE IF EXISTS Student")
conn.execute("CREATE TABLE IF NOT EXISTS Subject (subject TEXT PRIMARY KEY)")
conn.execute("CREATE TABLE IF NOT EXISTS SubjectModule (id INTEGER PRIMARY KEY AUTOINCREMENT,module TEXT, subject TEXT, FOREIGN KEY(subject) REFERENCES Subject(subject))")

conn.execute("INSERT INTO SubjectModule (module,subject) VALUES('','Software Engineering')")

conn.commit()
print("Database is running!")

app = QApplication(sys.argv)
window = stafflogin()
window.show()

app.exec()

