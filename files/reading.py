from pathlib import Path
import os
print(os.getcwd()) #لمعرفة الملف الذي نحن فيه الآن
#os.chdir(r'C:\Users\benha\Desktop')
print(Path.home())
print(os.getcwd())
#my_file = open(Path.home() / 'Desktop/salim.txt', 'r') هذه طريقة صحيحة
my_file = open(Path.home() / Path("Desktop","nwe", "salim.txt"), 'r')
print(str(Path.home() / Path("Desktop","nwe", "salim.txt")))

print(my_file)
print(my_file.name)
#print(my_file.read())
#print(my_file.read(9))#أول 9 حروف
#print(my_file.readlines())
lines = my_file.readlines()
print(lines[0:5])
i = 0
for line in lines:
    print(line)
    i += 1
    if i > 4:
        break

my_file.close()#إغلاق الملف

