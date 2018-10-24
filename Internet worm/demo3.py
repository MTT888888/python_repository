import requests
from bs4 import BeautifulSoup
url="http://www.baidu.com"
r=requests.get(url)
r.encoding=r.apparent_encoding
print(r.text)
demo=r.text
soup=BeautifulSoup(open("D://pics//388882.html"),"html.parser")
print(soup.prettify())