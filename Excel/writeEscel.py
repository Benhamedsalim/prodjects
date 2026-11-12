import openpyxl
from pathlib import Path
import os

#create excel file

excelFile = openpyxl.Workbook()
print(excelFile.sheetnames)
print(os.getcwd())

#change sheet name

excelSheet = excelFile.active
excelSheet.title = 'First_Sheet'

#create sheet

excelFile.create_sheet()
excelFile.create_sheet()
excelFile.create_sheet(index=1, title='secoundSheet')
excelFile.create_sheet(index=2, title='midelSheet')

#delelt sheet

del excelFile['midelSheet']

#Write to sheet

sheet = excelFile['secoundSheet']
sheet['A1'] = 'Hello world'
sheet['c2'] = 'Salim Benhamed'
print(sheet['A1'].value)
print(sheet['C2'].value)

#Write excel Practice
names = ['Salim', 'Moade', 'Bilal', 'Mohamed']
firsSheet = excelFile['First_Sheet']
for i in range(1, len(names)+1):
    firsSheet.cell(row= i, column= 3).value = names[i-1]


#save excel file

excelFile.save(filename= Path.home() / 'Desktop/test.xlsx')