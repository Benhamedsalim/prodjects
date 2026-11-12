import csv
from pathlib import Path

# file = open(Path.home() / Path('Desktop', 'CSV files', 'employees_2.csv'), "a", newline='')
# data = csv.DictWriter(file, ['Name', 'Salary', 'Date'], delimiter=';')
# data.writerow({'Name': 'Ali', 'Salary': '1500', 'Date':'05/12/2023'})
# file.close()


file = open(Path.home() / Path('Desktop', 'employees_test.csv'), 'w', newline='')
DictWriter = csv.DictWriter(file, ['Name', "Salary", 'Date' ])
DictWriter.writeheader()

DictWriter.writerow({'Name': 'Reem', 'Salary': '1500', 'Date': '04/09/2021'})
DictWriter.writerow({'Salary': '2500', 'Name': 'Hadi', 'Date': '04/09/2021'})
file.close()