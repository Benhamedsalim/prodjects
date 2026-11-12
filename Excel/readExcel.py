import openpyxl
from pathlib import Path

from openpyxl.styles.builtins import total

excelFile = openpyxl.load_workbook(Path.home() / 'Desktop/example.xlsx')
print(excelFile.sheetnames)

#sheet1 = excelFile[excelFile.sheetnames[0]]
sheet1 = excelFile['Sheet1']
print(sheet1.title)
activesheet = excelFile.active
print(activesheet)
print(sheet1['A1'].value)
print(sheet1['B1'].value)
print(sheet1['C1'].value)
print(sheet1['C1'].row)
print(sheet1['C1'].column)
print(sheet1['C1'].coordinate)
print(sheet1.cell(row=1, column=2).value)

#==========================================================================
print("-" * 17)
#==========================================================================

for i in range(1, 7):
    print(f"{i}. {sheet1.cell(row=i, column=1).value}")

#==========================================================================
print("-" * 17)
#==========================================================================
total = 0
for i in range(1, sheet1.max_row+1):
    print(f"{i}. {sheet1.cell(row=i, column=1).value}", f"{sheet1.cell(row=i, column=2).value}")
    total += sheet1.cell(row=i, column=2).value

print(f"The total salary of the employess {total}")

#==========================================================================
print("-" * 17)
#==========================================================================

print(sheet1.max_row)
print(sheet1.max_column)
