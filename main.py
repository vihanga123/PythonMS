import sys
import sqlite3
from sqlite3 import Connection
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QPushButton, QWidget
#from RegForm import register
from Login import stafflogin

conn: Connection = sqlite3.connect('Main.db')

conn.execute("CREATE TABLE IF NOT EXISTS Registration (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,DOB DATE,occupation TEXT,username TEXT,password TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,address TEXT,telephone INTEGER,course TEXT)")
# conn.execute("INSERT INTO users (username,password) VALUES('vihanga','123')")
conn.commit()
print("Database is running!")

cursor = conn.cursor()
#Prints Registration entries
cursor.execute("SELECT * FROM Registration")
rows = cursor.fetchall()
#for row in rows:
print(rows)

#Prints Student entries
cursor.execute("SELECT * FROM Student")
stud = cursor.fetchall()
#for row in stud:
print(stud)

app = QApplication(sys.argv)
window = stafflogin()
window.show()

app.exec()

