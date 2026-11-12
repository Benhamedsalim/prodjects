# employees = ['Hassan', 'Hadi', 'Salim', 'Ahmed']
#
# salary = [1000, 500, 2000, 600, 800]
#
# numbers = ['7645214781', '654789526', '4478965662', '998745625', '5547896456']

#Dictionaries
hadi = {
    'name': 'Hadi',
    'age': 22,
    'salary': 2000,
    'number': 7645214781,
    'skills': ['HTML', 'CSS', 'Bootstrap']

}
print(hadi)
print(hadi['name'])
print(hadi['salary'])
print(hadi['skills'])
#==================================================================
print("-" * 17)
#==================================================================
list = ['cats', 'dogs', 'moose']
my_list = ['dogs', 'moose', 'cats']
print(my_list == list)
print(my_list[0] == list[0])
print(my_list[1] == list[1])
print(my_list[0])
print(list[0])

#==================================================================
print("-" * 17)
#==================================================================

dictionary = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
myDictionary = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(dictionary == myDictionary)
print(dictionary['name'])
print(myDictionary['name'])

#==================================================================
print("-" * 17)
#==================================================================

# birthdays = {'hadi': 'Apr 1', 'sara': 'Dec 12', 'yara': 'Mar 4'}
# while True:
#     print('Enter a name: (blanck to quit)')
#     name = input()
#     if name == '':
#         break
#
#     if name in birthdays:
#         print(f'{name} was born in {birthdays[name]}')
#     else:
#         print((f'I don\'t know {name}'))
#         bday = input("What is theire birthday?:  ")
#         birthdays[name] = bday
#         print('Birthday database updated')

#==================================================================
print("-" * 17)
#==================================================================

hadi = {
    'name': 'Hadi',
    'age': 22,
    'salary': 2000,
    'number': 7645214781,
    'skills': ['HTML', 'CSS', 'Bootstrap']
}

print(hadi.keys())
print(hadi.values())
print(hadi.items())


salim = {
    'frontEnd' : {
        1: 'HTML',
        2: 'CSS',
        3: 'Bootstrap'
    },
    'backEnd': {
        1: 'PHP',
        2: 'Node.js'
    }
}
print(salim)
print(salim['frontEnd'])
print(salim['backEnd'])
print(salim['frontEnd'][2])

# تعيد الدالة ()items عرضًا جديدًا لعناصر القاموس بهيئة (مفتاح، قيمة).
# تعيد الدالة ()keys عرضًا جديدًا يتضمّن جميع مفاتيح القاموس.
# تستخدم الدالة ()values لعرض قيم المفاتيح الخاصة بالقاموس.
