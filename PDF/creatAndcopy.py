from PyPDF2 import PdfWriter as w
from pathlib import Path
import PyPDF2
#CREAT
pdf = w()
file = open(Path.home() / Path('Desktop', 'pdf_file.pdf'), "wb")

for i in range(5):
    pdf.add_blank_page(219, 297)
pdf.write(file)

#copy
pdffile = open(Path.home() / Path('Desktop', 'pdf_test.pdf'), "rb")
pdfReader = PyPDF2.PdfReader(pdffile)

for i in range(len(pdfReader.pages)):
    pdfObj = pdfReader.pages[i]
    pdf.add_page(pdfObj)
pdf.write(file)

file.close()