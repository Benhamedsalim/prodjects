import PyPDF2
from pathlib import Path
pdfFILEobj = open(Path.home() / "Desktop/pdf_test.pdf", "rb")
pdfReader = PyPDF2.PdfReader(pdfFILEobj)


print(len(pdfReader.pages))
pageobj = pdfReader.pages[0]
print(pageobj.extract_text())