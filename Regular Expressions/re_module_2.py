import re
from idlelib import search

# sub
string = """Hello my Number is 415-555-1011 and
my friend's number is 658-984-2165"""

replace = re.sub(r"\d{3}-\d{3}-\d{4}", r"658 984 2122", string, 1)
print(replace)
#==================================================================
print("-" * 17)
#==================================================================
txt = "Hello I'm student at hsoub academy"
replace = re.sub(r'hsoub academy', 'hsoub-academy', txt,)
print(replace)
#==================================================================
print("-" * 17)
#==================================================================
#split
search = re.split(r'\s', txt)
print(search)

search = re.split(r'\s', txt, 4)
print(search)

hsoub = "ستبدال-وتقطيع-النصوص-عبر-دوال-الوحدة"
replace = re.sub("-", ' ', hsoub)
print(replace)
#==================================================================
print("-" * 17)
#==================================================================
hsoub = "ستبدال-وتقطيع-النصوص-عبر-دوال-الوحدة"
replace = re.split("-", hsoub)
print(' '.join(replace))






