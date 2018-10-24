import requests
from bs4 import BeautifulSoup
import re

url="http://lib.zzu.edu.cn/article_list.aspx?sid=355dc7e7-f4c5-4ab7-a760-a30475ca55e6"
count=0
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    demo=r.text
    soup=BeautifulSoup(demo,"html.parser")
    for news in soup.select('.bd_R-li'):
          for news_1 in news.select('ul'):
            for news_2 in news_1.select('li'):
                title=news_2.select('a')[0].text
                url1=news_2.select("a")[0]['href']
                date=news_2.select('.spanR')[0].text
                count=count+1
                print("第",count,"条")
                print(title,url1,date)
except:
    print("抱歉！")
