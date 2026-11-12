import gspread
from gspread import worksheet
from oauth2client.service_account import ServiceAccountCredentials

scops = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scops)
client = gspread.authorize(credentials)
sheet = client.open("example")
# sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1S1c7mm5HhfUiPL-7DnlnX9Cne-v1svkS/edit?usp=sharing&ouid=115835247636656516494&rtpof=true&sd=true")

#worksheet = sheet.get_worksheet(0)
worksheet = sheet.worksheet("sheet1")
worksheet_list = sheet.worksheets()
print(worksheet_list)

#read from sheets
val = worksheet.acell("B1").value
print(val)
val = worksheet.acell("A1").value
print(val)
val = worksheet.cell(5,1).value
print(val)

values_list = worksheet.row_values(2)
print(values_list)

values_list = worksheet.col_values(1)
print(values_list)

list_of_lists = worksheet.get_all_values()
print(list_of_lists)
listOfDicts = worksheet.get_all_records()
print(listOfDicts)