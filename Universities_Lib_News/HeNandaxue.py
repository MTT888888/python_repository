import requests
from bs4 import BeautifulSoup
try:
    sum=0
    cum=0
    cout=0
    for i in range(1,2):
        cout=cout+1
        print("<<<<<<<<<<<<<<<<<<<<第",cout,"页>>>>>>>>>>>>>>>>>>>>>>")
        urls="http://lib.henu.edu.cn/list.jsp?a4t=40&a4p="+str(i)+"&a4c=15&urltype=tree.TreeTempUrl&wbtreeid=1017"
        r=requests.get(urls)
        r.encoding=r.apparent_encoding
        demo=r.text
        soup=BeautifulSoup(demo,"html.parser")
        news=soup.select('.c17990')
        news1=soup.select('.timestyle17990')
        for k in news:
            url="http://lib.henu.edu.cn/"+k.get("href")
            title=k.get("title")
            cum=cum+1
            print(cum, "  标题:" + title, "\n", "    链接:" + url)
        for j in news1:
            date=j.text
            sum=sum+1
            print(sum,"  时间:" + date)
except:
     print("抱歉！")