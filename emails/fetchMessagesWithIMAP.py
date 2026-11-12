import imapclient
import pprint
import pyzmail

#contact to verver
imapOBJ = imapclient.IMAPClient('imap.gmail.com', ssl=True)
#login to email
res_email = '.........'
password = input('Enter your password: ')
imapOBJ.login(res_email, password)

#print all folders
pprint.pprint(imapOBJ.list_folders())

# select folder
imapOBJ.select_folder('INBOX', readonly=True)

#search in folder
UIDs = imapOBJ.search('ALL')
#print(UIDs)
rawMessages = imapOBJ.fetch(UIDs, ['BODY[]'])
#pprint.pprint(rawMessages)
message = pyzmail.PyzMessage().factory(rawMessages[73]['BODY[]'])
# print(message.get_subject())
# print(message.get_addresses('from'))
# print(message.get_addresses('to'))

# get message body
print(message.text_part.get_payload().decode(message.text_part.charset))
print(message.html_part.get_payload().decode(message.text_part.charset))

imapOBJ.logout()