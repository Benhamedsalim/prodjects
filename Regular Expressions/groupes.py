#Groupes
import re
phone = "415-555-1234"
search = re.search(r"(\d{3})-(\d{3}-\d{4})", phone)

print(search.group())
print(search.group(0))
print(search.group(1))
print(search.group(2))
#==================================================================
print("-" * 17)
#==================================================================
date = '29-11-1996'
search = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)
day = search.group(1)
month = search.group(2)
years = search.group(3)
print('The day of the month is', day, 'the month is', month, 'and the year is', years)
day, month, years = search.groups()
print('The day of the month is', day, 'the month is', month, 'and the year is', years)

