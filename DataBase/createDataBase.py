import sqlite3
from pathlib import Path

sqliteConnection = sqlite3.connect(Path.home() / Path("Desktop", 'database.db'))
crsr = sqliteConnection.cursor()
print('Connected to database')
#SQL command to create a table in the database

sql_command = """ CREATE TABLE IF NOT EXISTS students (
 firstname VARCHAR(20),
 lastname VARCHAR(20),
 AGE INT)"""
crsr.execute(sql_command)
#INSERT DATA
crsr.execute("INSERT INTO students VALUES ('Hadi', 'Hassan', '23');")
crsr.execute("INSERT INTO students VALUES ('Salim', 'Benhamed', '30');")
crsr.execute("INSERT INTO students VALUES ('Morad', 'Sali', '25');")
sqliteConnection.commit()
#close to connection
sqliteConnection.close()
