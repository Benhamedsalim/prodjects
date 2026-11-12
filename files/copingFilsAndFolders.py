import shutil
from pathlib import Path

shutil.copy(Path.home() / Path('desktop', 'nwe', 'salim.txt'), Path.home() / Path('desktop', 'Salim_copied.txt'))
shutil.copytree(Path.home() / Path('desktop', 'nwe'), Path.home() / Path('desktop','new'))






