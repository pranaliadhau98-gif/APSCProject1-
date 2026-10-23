
import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE registration (
    Role TEXT,
    Adhar_No TEXT,
    Full_Name TEXT,
    Gender TEXT,
    Mobile_No INTEGER,
    Address TEXT,
    DOB TEXT
)''')

conn.commit()

cursor.execute('SELECT * FROM registration')
result = cursor.fetchone()

print(result)

conn.close()
