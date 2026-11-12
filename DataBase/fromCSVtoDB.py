import csv
import sqlite3
from pathlib import Path


#CONNECT
sqliteConnections = sqlite3.connect(Path.home() / Path("Desktop", 'database.db'))
crsrs = sqliteConnections.cursor()
print('Connected to database')

sql_commands = """ CREATE TABLE IF NOT EXISTS employees_1 (
id INTEGER,
Name VARCHAR(20),
Salary INTEGER,
dataOfEmployment TEXT)"""
crsrs.execute(sql_commands)

# read file
file = open(Path.home() / Path('Desktop', 'employees_1.csv'))
rows = csv.reader(file)

# add data to table
crsrs.executemany("INSERT INTO employees_1 VALUES (?, ?, ?, ?)", rows)

sqliteConnections.commit()


sqliteConnections.close()