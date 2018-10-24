import requests
from bs4 import BeautifulSoup
sum=0
count = 0
try:
    for i in range(1,2):
        urls="http://lib.henau.edu.cn/Default/go?sortID=109&startIndex="+str(i*15)
        r=requests.get(urls)
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,"html.parser")
        print(soup)
        news=soup.find_all(class_="left")
        print(news)












                    # print(sum,"  标题:",title,'\n','    链接:',url1,'\n',"    日期:",date)
except:
    print("抱歉!")


