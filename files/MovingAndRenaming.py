import shutil
from pathlib import Path
myFile = open(Path.home() / Path('Desktop','nwe','salim.txt'), 'a')
myFile.write('12. Hello, how are you\n')
myFile.write('13. Hello, how are you\n')
myFile.close()
#shutil.move(Path.home() / Path('Desktop','nwe', 'rest.txt'), Path.home() / Path('Desktop','new'))
shutil.move(Path.home() / Path('Desktop','nwe', 'salim.txt'), Path.home() / Path('Desktop','nwe', "Benhamed Salim.txt"))
