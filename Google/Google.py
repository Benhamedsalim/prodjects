import gspread
from oauth2client.service_account import ServiceAccountCredentials

scops = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scops)
client = gspread.authorize(credentials)
sheet = client.open("test").sheet1
sheet.update_cell(2, 1, "Hello World")


