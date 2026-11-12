from asyncio import exceptions

import openpyxl
from pathlib import Path
from openpyxl.styles import Font
import sys

if len(sys.argv) == 2:
    try:
        number = int(sys.argv[1])
    except exceptions as e:
        print(e)
    excelfile = openpyxl.Workbook()
    sheet = excelfile.active

    for x in range(number + 1):
        for y in range(number + 1):
            #check if header row or column

            isheader = False
            if x == 0 and y == 0:
                isheader = True
                n = ''
            elif x == 0:
                isheader = True
                n = y
            elif y == 0:
                isheader = True
                n = x
            else:
                n = x * y
            cell = sheet.cell(row=y +1,column=x +1)

            if isheader:
                cell.font = Font(bold=True)
            cell.value = n
    savedFile = str(Path.home() / Path('Desktop') / 'multiplication_Tabel_') + str(number) + '.xlsx'
    excelfile.save(savedFile)

    print(f'Save as {savedFile}')





else:
    print("Please enter only TWO arguments")