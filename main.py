import sys
import sqlite3
from sqlite3 import Connection
from PySide6.QtWidgets import QApplication
from Login import stafflogin


# Database creation
conn: Connection = sqlite3.connect('Main.db')

# Enables SQlite foreign key otherwise default disabled
conn.execute('PRAGMA foreign_keys = ON')

# Table creation (if not already exists)
conn.execute("CREATE TABLE IF NOT EXISTS Registration (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,DOB DATE,occupation TEXT,username TEXT,password TEXT)")
conn.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,age INTEGER,address TEXT,telephone INTEGER,subject TEXT, FOREIGN KEY(subject) REFERENCES Subject(subject))")
conn.execute("CREATE TABLE IF NOT EXISTS Subject (subject TEXT PRIMARY KEY)")
conn.execute("CREATE TABLE IF NOT EXISTS SubjectModule (id INTEGER PRIMARY KEY AUTOINCREMENT,module TEXT, subject TEXT, FOREIGN KEY(subject) REFERENCES Subject(subject))")
conn.execute("CREATE TABLE IF NOT EXISTS StudentGrade (sid INTEGER, mid INTEGER, subject TEXT, grade TEXT, FOREIGN KEY(subject) REFERENCES Subject(subject),FOREIGN KEY(mid) REFERENCES SubjectModule(id),FOREIGN KEY(sid) REFERENCES Student(id))")

# Adds the necessary data into the table (if not already exists)
conn.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?", ('0', "SubjectModule"))
conn.commit()

x = 0
subjects = ["Application Development", "Software Engineering", "Network Engineering"]
AP = ["GUI Design", "Mobile App Development", "Computer Technology"]
SW = ["Mathematics", "OOP", "Database Management"]
NE = ["Data Communication", "Database Management", "Routing and Switching"]
while x < len(subjects):
    conn.execute("INSERT OR IGNORE INTO Subject(subject) VALUES(?)", [subjects[x]])
    x += 1
    conn.commit()

n = 0
y = 0
while y < len(AP):
    conn.execute("INSERT OR IGNORE INTO SubjectModule(id, module, subject) VALUES(?, ?, ?)", [n, AP[y], subjects[0]])
    y += 1
    n += 1
    conn.commit()

y = 0
while y < len(SW):
    conn.execute("INSERT OR IGNORE INTO SubjectModule(id, module, subject) VALUES(?, ?, ?)", [n, SW[y], subjects[1]])
    y += 1
    n += 1
    conn.commit()

y = 0
while y < len(NE):
    conn.execute("INSERT OR IGNORE INTO SubjectModule(id, module, subject) VALUES(?, ?, ?)", [n, NE[y], subjects[2]])
    y += 1
    n += 1
    conn.commit()

# Changes the auto increment value of the sequence to the amount of records in the student table.
cursor = conn.execute("SELECT count(*) FROM Student;")
info = cursor.fetchone()[0]
conn.execute("UPDATE sqlite_sequence SET seq = ? WHERE name = ?", (info, "Student"))
conn.commit()

print("Database is running!")

# Runs the login page Qt python window
app = QApplication(sys.argv)
window = stafflogin()
window.show()

app.exec()

