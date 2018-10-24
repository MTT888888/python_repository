import requests
from bs4 import BeautifulSoup
import re
count=0
sum=0
try:

    for i in range(0,20):
        urls="http://lib.haust.edu.cn/haust/include/annmessage.jsp?id=17&pager.offset="+str(i*10)
        count=count+1
        print("<<<<<<<<<<<<<<<<<<<<<<",count,">>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        r=requests.get(urls)
        r.encoding=r.apparent_encoding
        soup=BeautifulSoup(r.text,"html.parser")
        news=soup.select(".list_icon")
        for news1 in news:
            news2=news1.select("li")
            for news3 in news2:
                title=news3.select("a")[0]["title"]
                url="http://lib.haust.edu.cn"+news3.select("a")[0]["href"]
                pattern=re.compile(r"([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))")
                date=re.search(pattern,str(news3))
                sum = sum + 1
                print(sum, "  标题:", title, "\n", "    链接:", url,"\n","    日期:",date.group())
except:
    print("Sorry！")