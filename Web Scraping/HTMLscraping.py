import bs4
import requests
from real_useragent import UserAgent

ua = UserAgent()
headers = {"User-Agent": ua.random_useragent()}
res = requests.get("https://en.wikipedia.org/wiki/Main_Page", headers=headers)
#print(res.text)
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(noStarchSoup))

element = noStarchSoup.select('#mp-tfa > p')
print(element)
print(element[0].getText())
