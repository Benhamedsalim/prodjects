#get()
hadi = {
    'name': 'Hadi',
    'age': 22,
    #'salary': 2000,
    'number': 7645214781,
    'skills': ['HTML', 'CSS', 'Bootstrap']

}

#print(f"{hadi['name']} receives a salary of {hadi['salary']}")

print(f"{hadi['name']} receives a salary of {hadi.get('salary', 'no salary')}")

#==================================================================
print("-" * 17)
#==================================================================
# setdefault
print(hadi)
print(hadi.setdefault('name','Ramzy'))
print(hadi)
print(hadi.setdefault('salary','2000'))
print(hadi)
if 'language' not in hadi:
    hadi['language'] = 'Python'
print(hadi)
#==================================================================
print("-" * 17)
#==================================================================
#update
numbers = {
    1: 'one',
    2: 'three',
}
print(numbers)
numbers.update({2:'two'})
print(numbers)
numbers.update({3:'three'})
print(numbers)

#==================================================================
print("-" * 17)
#==================================================================
#clear
print(hadi)
hadi.clear()
print(hadi)