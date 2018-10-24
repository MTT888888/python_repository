from openpyxl import workbook
import pandas as pd
import requests
from bs4 import BeautifulSoup
try:
    cout=0
    sum=0
    # with open('D:河南省大学名单.text','w',encoding='utf-8') as f:

    url="http://www.gaosan.com/gaokao/150677.html"
    headers={ 'User-Agent':
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0' }
    r=requests.get(url,headers=headers)
    r.encoding=r.apparent_encoding
    soup=BeautifulSoup(r.text,'html.parser')
    t1=soup.select("#data150677")
    for t2 in t1:
        t3 = t2.select('tr')
        for t4 in t3:
            xuexiao= t4.select('td:nth-of-type(1)')[0].text
            daima=t4.select('td:nth-of-type(2)')[0].text
            zhuguan=t4.select('td:nth-of-type(3)')[0].text
            dizhi=t4.select('td:nth-of-type(4)')[0].text
            cengci=t4.select('td:nth-of-type(5)')[0].text
            beizhu=t4.select('td:nth-of-type(6)')[0].text
            cout=cout+1
            print(cout,  xuexiao,daima,zhuguan,dizhi,cengci,beizhu)

                # f.write("{}   {}               {}              {}              {}               {}              {}\n".format(cout,xuexiao,daima,zhuguan,dizhi,cengci,beizhu))

except:
    print("哈哈")


