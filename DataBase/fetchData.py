import sqlite3
from pathlib import Path

# Connect
sqliteConnection =sqlite3.connect(Path.home() / Path('Desktop', 'dataBase.db'))
crsr = sqliteConnection.cursor()
print("Connected to the database")

crsr.execute("SELECT Name, Salary, dataOfEmployment FROM employees_1 where Salary > 850")
#print(crsr.fetchall())
#print(crsr.fetchone())
#print(crsr.fetchmany(3))

anser = crsr.fetchall()
for i in anser:
    print(i)