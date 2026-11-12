import shutil
import os
import re
from pathlib import Path

date = datePattern = "^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$"
for i in os.listdir(Path.home() / Path('Desktop', 'files')):
    search = re.search(datePattern, i)

    if search == None:
        continue
    beforePart = search.group(1)
    monthPart = search.group(2)
    dayPart = search.group(4)
    yearPart = search.group(6)
    afterPart = search.group(8)

    nweFileNme = beforePart + dayPart + '-' +  monthPart + '-' + yearPart + afterPart
    print(f'"Renaming" {i} to "{nweFileNme}"')

    oldname = Path.home() / Path('Desktop', 'files') / nweFileNme
    nwename = Path.home() / Path('Desktop', 'files') / nweFileNme
    shutil.move(oldname, nwename)