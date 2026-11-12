#append, insert
employees = ['Hassan', 'Hadi', 'Salim', 'Ahmed']
print(employees)
# employees.append('Morad')
# print(employees)
# employees.insert(1,'Ramzy')
# print(employees)
#
#
oldemployees = ['Ossama', 'Sammy']
# employees.append(oldemployees)
# print(employees)
# print(employees[6])
# print(employees[6][0])
#==================================================================
print("-" * 17)
#==================================================================
employees.extend(oldemployees)
print(employees)
#==================================================================
print("-" * 17)
#==================================================================
#remove

employees.remove('Ossama')
print(employees)

#==================================================================
print("-" * 17)
#==================================================================
#del statment
del employees[0]
print(employees)
del employees[-1]
print(employees)

#==================================================================
print("-" * 17)
#==================================================================
#sort
employees.sort()
print(employees)
employees.sort(reverse=True)
print(employees)
nembers = [2, 5, 3.14, 1, -7]
nembers.sort()
print(nembers)
nembers.sort(reverse=True)
print(nembers)

#==================================================================
print("-" * 17)
#==================================================================
#reverse
employees = ['Hassan', 'Hadi', 'Salim', 'Ahmed']
employees.reverse()
print(employees)

#
# تضيف الدالة ()append عنصر إلى نهاية القائمة.
# تضيف الدالة ()extend مجموعة من العناصر إلى نهاية القائمة.
# تضيف الدالة ()insert عنصر إلى القائمة في الموقع الذي يحدّده المستخدم.
# تحذف الكلمة المفتاحية del الكائنات باختلاف أنواعها (قائمة أو سلسلة أو قاموس ..إلخ).
# تحذف الدالة ()remove أول عنصر في القائمة تساوي قيمته القيمة التي يحدّدها المستخدم.
# تحذف الدالة ()pop العنصر في الموقع المحدّد من قبل المستخدم.
# تستخدم الدالة ()sort في بايثون لفرز القائمة في مكانها وذلك بإجراء مقارنة بين عناصر القائمة بواسطة العامل > فقط.