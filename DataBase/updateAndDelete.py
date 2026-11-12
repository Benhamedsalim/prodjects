import sqlite3
from pathlib import Path


#CONNECT
sqliteConnections = sqlite3.connect(Path.home() / Path("Desktop", 'database.db'))
crsr = sqliteConnections.cursor()
print('Connected to database')

#Updating
crsr.execute("UPDATE employees_1 SET Salary = 600 WHERE id = 5")

#DELETING
crsr.execute("DELETE FROM employees_1 WHERE id = 4")

crsr.execute("UPDATE employees_1 SET id = id - 1 WHERE id > 3")

sqliteConnections.commit()

sqliteConnections.close()