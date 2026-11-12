import ezgmail

print(ezgmail.EMAIL_ADDRESS)

# ezgmail.send("......", "Test line", "Yes i'm man how leads the black knghits and change the world", ['test.png', 'test1.png'])

# get the unread message
unreadmessage = ezgmail.unread()

# print(ezgmail.summary(unreadmessage))
# print(unreadmessage[0].messages[0])
# print(unreadmessage[0].messages[0].subject)
# print(unreadmessage[0].messages[0].body)
# print(unreadmessage[0].messages[0].timestamp)
# print(unreadmessage[0].messages[0].sender)
# print(unreadmessage[0].messages[0].recipient)

# get the recend messages
# reczndThreads = ezgmail.recent()
# print(len(reczndThreads))
#
# reczndThreads = ezgmail.recent(maxResults=10000)
# print(len(reczndThreads))

# Search
reczndThreads = ezgmail.search('gmail')
print(len(reczndThreads))