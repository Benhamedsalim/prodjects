import random

employees = ['Hassan', 'Hadi', 'Salim', 'Ahmed']
# print(employees)
# print(employees[0])
# print(employees[2])
# print(employees[-1])
# print(employees[-2])
# print(employees[:2])
# print(employees[:-1])
# print(employees[-2:])
# print(employees[::-1])
# print(employees)
# employees[1] = 'Ramzy'
# print(employees)
# print(employees[1:3])
# employees[0:2] = 'Issam', 'Nabil'
# print(employees)
# employees[0:3:2] = 'Salim', 'Hassan'
# print(employees)
# employees[2:] = ''
# print(employees)

#==================================================================
print("-" * 17)
#==================================================================
#for loop
# for employee in employees:
#     print(employee, end=', ')
# print()
# for i in range(len(employees)):
#     print(employees[i], end=', ')
# print()
# for i in range(len(employees)):
#     print(f'Index {i} in employees is: {employees[i]}')

#==================================================================
print("-" * 17)
#==================================================================
#enumerate
# for index, item in enumerate(employees):
#     print(f'Index {index} in employees is: {item}')

#==================================================================
print("-" * 17)
#==================================================================
#in, not in
# print('Hadi'in employees)
# print('Samir' not in employees)
# name = input("أدخل إسم الموظف : ").capitalize()
# if name not in employees:
#     print(f"ليس لدينا موظف بهذا الإسم {name}")
# else:
#     print(f' هو موظف في الشركة{name}')

#==================================================================
print("-" * 17)
#==================================================================
#ranmod.choice, random.shuffle
import random

print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
random.shuffle(employees)
print(employees)
print(employees)


