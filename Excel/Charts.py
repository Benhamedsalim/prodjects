import openpyxl
from pathlib import Path
excelFile = openpyxl.load_workbook(Path.home() / Path('Desktop', 'example.xlsx'))
sheet = excelFile['Sheet1']

#charts

title = openpyxl.chart.Reference(sheet, min_col=1, max_col=1, min_row=1, max_row=sheet.max_row)
data = openpyxl.chart.Reference(sheet, min_col=2, max_col=2, min_row=1, max_row=sheet.max_row)

chart = openpyxl.chart.PieChart()
chart.title = 'My chart'
chart.add_data(data=data)
chart.set_categories(title)
sheet.add_chart(chart, 'E8')

excelFile.save(filename= Path.home() / Path('Desktop', 'example.xlsx'))
