import sqlite3
import random

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
bal INTEGER NOT NULL
)
''')

cursor.execute(" CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

#for i in range(10):
#    cursor.execute(" INSERT INTO Users (username, email, age, bal) VALUES (?, ?, ?, ?)",
#                   (f"user{i}", f"ex{i}@gmail.com", str(random.randint(20, 60)), 1000))

#for i in range(10):
#     if i % 2 == 0:
#         n = i + 1
#         cursor.execute("UPDATE Users SET bal = ? WHERE id = ?", (500, f"{n}"))

#for i in range(10):
#     if i % 3 == 0:
#         n = i + 1
#         cursor.execute("DELETE FROM Users WHERE id = ?", (f"{n}",))

connection.commit()
connection.close()