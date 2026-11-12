import os
from pathlib import Path
import shutil
import send2trash
#os.unlink(Path.home() / Path('Desktop','nwe','Benhamed salim.txt'))
#os.rmdir(Path.home() / Path('Desktop','new'))
#shutil.rmtree(Path.home() / Path('Desktop','new', 'nwe folder'))
send2trash.send2trash(Path.home() / Path('Desktop', 'new', 'new folder'))
send2trash.send2trash(Path.home() / Path('Desktop', 'new', 'rest.txt'))
