import sys
import sqlite3
from sqlite3 import Connection
from PySide6.QtWidgets import QApplication
from Login import stafflogin

conn: Connection = sqlite3.connect('Main.db')
conn.execute('PRAGMA foreign_keys = ON')

conn.execute("CREATE TABLE IF NOT EXISTS Registration (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,DOB DATE,occupation TEXT,username TEXT,password TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,address TEXT,telephone INTEGER,subject TEXT, FOREIGN KEY(subject) REFERENCES Subject(subject))")
#conn.execute("DROP TABLE IF EXISTS StudentGrade")
conn.execute("CREATE TABLE IF NOT EXISTS Subject (subject TEXT PRIMARY KEY)")
conn.execute("CREATE TABLE IF NOT EXISTS SubjectModule (id INTEGER PRIMARY KEY AUTOINCREMENT,module TEXT, subject TEXT, FOREIGN KEY(subject) REFERENCES Subject(subjects))")
conn.execute("CREATE TABLE IF NOT EXISTS StudentGrade (sid INTEGER, mid INTEGER, subject TEXT, grade TEXT, FOREIGN KEY(subject) REFERENCES Subject(subject),FOREIGN KEY(mid) REFERENCES SubjectModule(id),FOREIGN KEY(sid) REFERENCES Student(id))")

#conn.execute("INSERT INTO StudentGrade (sid,mid,subject,grade) VALUES('1','9','Software Engineering','70')")

cursor = conn.execute("SELECT * FROM SubjectModule")
all = cursor.fetchall()
for row in all:
    print (row)

cursor = conn.execute("SELECT * FROM StudentGrade")
all1 = cursor.fetchall()
for row1 in all1:
    print (row1)

#conn.execute("INSERT INTO SubjectModule (module,subject) VALUES('Computer Technology','Application Development')")

#Changes the auto increment value of the sequence to the amount of records in the student table.
cursor = conn.execute("SELECT count(*) FROM Student;")
info = cursor.fetchone()[0]

conn.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?", (info, "Student"))

conn.commit()
print("Database is running!")

app = QApplication(sys.argv)
window = stafflogin()
window.show()

app.exec()

