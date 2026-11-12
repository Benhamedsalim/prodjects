import openpyxl, smtplib
from pathlib import Path

file = openpyxl.load_workbook(Path.home() / Path("Desktop", "members.xlsx"))

sheets = file.sheetnames
sheet = file[sheets[0]]
lastcole = sheet.max_column
letestMonth = sheet.cell(row=1, column=lastcole).value
print(letestMonth)

#find unpaid members
unpaidMmbers = {}
for r in range(2, sheet.max_row + 1):
    payment = sheet.cell(row=r, column=lastcole).value
    if payment != 'paid':
        name = sheet.cell(row=r, column=1).value
        email = sheet.cell(row=r, column=2).value
        unpaidMmbers[name] = email

#send email
smtpOBJ = smtplib.SMTP('smtp.gmail.com', 587)
smtpOBJ.starttls()
sender_email = '.......'
password = input('Enter your password: ')
smtpOBJ.login(sender_email, password)

for name, email in unpaidMmbers.items():
    body = """SUBJECT: %s dues unpaid.\nDear %s,\nRecords show that you have nt paid dues for %s. Make this payment as soon as possible. Thank you! """ % (letestMonth, name, letestMonth)
    print("Sending email to %s..." % email)
    sendmailstatu = smtpOBJ.sendmail(sender_email, email, body)
    if sendmailstatu != {}:
        print('there was a problem sending email to %s: %s' % (name, sendmailstatu))

smtpOBJ.quit()