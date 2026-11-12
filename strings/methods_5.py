#index(substring, start, end)
text = 'Holle world'
print(text.index('world'))
print(text.index('o'))
#print(text.index('world', 0, 5))
try:
    print(text.index('world', 0, 5))
except ValueError:
    print('No error')
#==================================================================
print("-" * 17)
#==================================================================
#find(substring, start, end)
text = 'Holle world'
print(text.find('world'))
print(text.find('world', 0, 5))
#==================================================================
print("-" * 17)
#==================================================================
#replace(old value, new value, count)
test = "One plus one egual two".lower()
print(test)
print(test.replace('one', '1'))
print(test.replace('one', '1', 1))


