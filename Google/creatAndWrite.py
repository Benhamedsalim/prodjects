from xmlrpc import client

import gspread
from oauth2client import file
from oauth2client.service_account import ServiceAccountCredentials

scops = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
]

credentials = ServiceAccountCredentials.from_json_keyfile_name('keys.json', scops)
client = gspread.authorize(credentials)

#creat new file
# new_client = client.create('A new spreadsheet')
# new_client.share("salimfullmetal@gmail.com", perm_type="user", role="owner")

new_client = client.open('A new spreadsheet')
#creat nwe sheet
worksheet = new_client.add_worksheet(title="Sheet2", rows="100", cols="20")