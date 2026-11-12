import zipfile
from pathlib import Path
import os
import shutil
compresszip = zipfile.ZipFile(Path.home() / Path('Desktop', 'new.zip'))
print(compresszip.namelist())
fileInfo = compresszip.getinfo('new/salim.txt')
print(fileInfo.file_size)
print(fileInfo.compress_size)

#extract
os.chdir(Path.home() / Path('Desktop'))
compresszip.extractall()
compresszip.extract('new/salim.txt', Path.home() / Path('Desktop', 'extsractFiles'))

print(os.getcwd())
nweZip = zipfile.ZipFile('new1.zip', "w")
nweZip.write('new/salim.txt')

#compressFolder
folderZip = zipfile.ZipFile('new2.zip', "w")
folderZip.write('new')

shutil.make_archive("compressFolder", 'zip', Path.home() / Path('Desktop', 'new'))