from bs4 import BeautifulSoup
import requests
url="http://www.baidu.com"
r=requests.get(url)
# print(r.status_code)
r.encoding=r.apparent_encoding
# print(r.text)
demo=r.text
soup=BeautifulSoup(demo,"html.parser")
for link in soup.find_all('a'):
    print(link.get("href"))