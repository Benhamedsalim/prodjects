import os, csv
from pathlib import Path

os.makedirs(Path.home() / Path('Desktop', 'CSV files'), exist_ok=True)

for csvfilename in os.listdir(Path.home() / Path('Desktop', 'CSV files')):
    if not csvfilename.endswith('.csv'):
        continue

    print('Removing Header from ' + csvfilename, '...')
    csvRows = []
    csvFileobj = open(Path.home() / Path('Desktop', 'CSV files', csvfilename))
    readerobj = csv.reader(csvFileobj)


    for row in readerobj:
        if readerobj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileobj.close()

    csvFileobj = open(Path.home() / Path('Desktop', 'CSV files', csvfilename), 'w', newline='')
    csvWriter = csv.writer(csvFileobj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileobj.close()