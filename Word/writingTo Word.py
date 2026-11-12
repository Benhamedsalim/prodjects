import docx
from pathlib import Path
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from openpyxl.chart.title import Title

mydoc = docx.Document()
mydoc.add_paragraph("This the firs paragraph")
mydoc.add_paragraph("This the firs paragraph again")

#إضافة حملة بالعربية
paragraph = mydoc.add_paragraph("هذه هي الفقرة الثالثة")
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

third_paragraph = mydoc.add_paragraph('This the third paragraph')
third_paragraph.add_run("This the third paragraph again")

#add heading
mydoc.add_heading("This the first heading", 0)
mydoc.add_heading("This the first heading", 1)
mydoc.add_heading("This the first heading", 2)
mydoc.add_heading("This the first heading", 3)
mydoc.add_heading("This the first heading", 4)
mydoc.add_heading("This the first heading", 5)

#style
print(mydoc.paragraphs[0].style)
print(mydoc.paragraphs[5].style)
print(mydoc.paragraphs[4].style)
mydoc.paragraphs[0].style = mydoc.styles['Heading 1']
mydoc.paragraphs[3].style = mydoc.styles['Heading 4']
mydoc.paragraphs[3].style.delete()

mydoc.add_paragraph('This is the style paragraph', "Title")
#add image
mydoc.add_picture(str(Path.home() / Path("Desktop", "AI-ML-Full-cover.png.00c26f7c8f0958a7b9d331895d5a313e.png")), width=docx.shared.Inches(5), height=docx.shared.Inches(7))


mydoc.save(Path.home() / "Desktop/write.docx")