import ezgmail, os
from pathlib import Path

os.chdir(Path.home() / Path("Desktop", 'Prodject', 'emails'))
ezgmail.init()