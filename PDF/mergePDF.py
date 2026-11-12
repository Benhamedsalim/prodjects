import PyPDF2, os
from pathlib import Path

pdffile =[]
for i in os.listdir(Path.home() / Path('Desktop', 'article')):
    if i.endswith(".pdf"):
        pdffile.append(i)

pdffile.sort(key=str.lower)
PdfWriter = PyPDF2.PdfWriter()
for x in pdffile:
    pdffobj = open(Path.home() / Path('Desktop', 'article', x), 'rb')
    pdfreader = PyPDF2.PdfReader(pdffobj)
    for page in range(1, len(pdfreader.pages)):
        pageobj = pdfreader.pages[page]
        PdfWriter.add_page(pageobj)

pdfoutput = open(Path.home() / Path("Desktop", 'article', 'article.pdf'), 'wb')
PdfWriter.write(pdfoutput)
pdfoutput.close()

