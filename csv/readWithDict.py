import csv
from pathlib import Path

file = open(Path.home() / Path('Desktop', 'CSV files', 'employees_2.csv'))
data = csv.DictReader(file)
for row in data:
    print(row["Name"], row["Salary"], row["Date"])
