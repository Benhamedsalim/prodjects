from pathlib import Path

myFile = open('salim.txt', 'w')
myFile = open(Path.home() / Path('Desktop','nwe','salim.txt'), 'a')
myFile.write('\n11. Hello, how are you\n')
myFile.write('12. Hello, how are you\n')
myFile.write('13. Hello, how are you\n')

# writelines
# myList = ['\n14. Hello, how are you\n', '15. Hello, how are you\n', '16. Hello, how are you\n']
# myFile.writelines(myList)