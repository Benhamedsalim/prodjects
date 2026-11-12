from pdf2docx import Converter
from pathlib import Path

pdf_file = Path.home() / Path("Desktop", "article.pdf")
docx_file = Path.home() / Path("Desktop", "articleConverter.docx")

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start= 2, end= 6)
#cv.convert(docx_file)
cv.close()

