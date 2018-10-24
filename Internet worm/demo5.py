import requests
from bs4 import BeautifulSoup
import bs4
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=20)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return " "

def fillUnivList(list,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.findAll('tobody'):
        if isinstance(tr,bs4.elememt.Tag):
            tds=tr('td')
            list.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList(list,number):
    print("{:^10}\t{:^6}\t{:^10}".format("排名","学校名称","总分"))
    for i in range(number) :
        u=list[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
def main():
    ulist=[]
    url='http://www.zuihaodaxue.cn/shengyuanzhiliangpaiming2018.html'
    html=getHTMLText(url)
    fillUnivList(ulist,html)
    printUnivList(ulist,20)
if __name__ == '__main__':
    main()
