import sqlite3
import pandas as pd

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students
                  (id INTEGER, name TEXT)""")

cursor.execute("INSERT INTO students VALUES (1, 'John')")
conn.commit()

df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)

cursor.execute("UPDATE students SET name = 'Alice' WHERE id = 1")
cursor.execute("DELETE FROM students WHERE id = 1")

conn.commit()
conn.close()