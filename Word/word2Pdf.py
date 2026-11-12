from pathlib import Path
from docx2pdf import convert

docx_file = Path.home() / Path('Desktop', 'write.docx')

pdf_file = Path.home() / Path('Desktop', 'write.pdf')

multi_file = Path.home() / Path('Desktop', 'Word files/')

convert(multi_file)