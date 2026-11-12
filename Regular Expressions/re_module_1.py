import re

#search
txt = "My name is Salim"
search = re.search('[A-Z]', txt)
print(search)
print(search.span())
print(dir(search))
print(search.group())

test = "Call me at 123-123-1234 tomorow. 234-567-7890 is my office"
search = re.search(r"\d{3}-\d{3}-\d{4}", test)
print(search)
print(search.string)
print(search.group())