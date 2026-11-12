import bs4
from pathlib import Path

exampleFile = open(Path.home() / "Desktop/example.html")
exanplesoup = bs4.BeautifulSoup(exampleFile, "html.parser")
print(type(exanplesoup))

element = exanplesoup.select('p')
print(type(element))
print(element)
print(len(element))
print(element[0].getText())
print(element[1].attrs)