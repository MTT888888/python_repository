import requests
from bs4 import BeautifulSoup
# db_config ={
#     'host': '202.196.37.91',#连接的主机id(107.0.0.1是本机id)
#     'port': 3306,
#     'user': 'zutnlp',
#     'password': 'zutnlp',
#     'db': 'henanlibrary',#（数据库名）
#     'charset': 'utf8'
# }

sum=0
count=0
try:
    for i in range(1,21):
        count=count+1
        print("<<<<<<<<<<<<<<<<<<<<",count,">>>>>>>>>>>>>>>>>>>>>>>>")
        urls="http://lib.shengda.edu.cn/xwgg/"+str(i)+".htm"
        r=requests.get(urls)
        r.encoding=r.apparent_encoding
        demo=r.text
        soup=BeautifulSoup(demo,"html.parser")
        for j in soup.select(".main_conRCb"):
            for k in j.select("li"):
                for n in k.select("a"):
                    title=n.select("em")[0].text
                    url1="http://lib.shengda.edu.cn"+n.get("href")[2:]
                    date=n.select("span")[0].text
                    sum=sum+1
                    print(sum,"  标题:",title,'\n','    链接:',url1,'\n',"    日期:",date)
except:
    print("Sorry!")
#
#         # 获得数据库游标（游标提供了一种对从表中检索出的数据进行操作的灵活手段，就本质而言，游标实际上是一种能从包括多条数据记录的结果集中每次提取一条记录的机制。游标总是与一条SQL 选择语句相关联因为游标由结果集（可以是零条、一条或由相关的选择语句检索出的多条记录）和结果集中指向特定记录的游标位置组成。）
#         with connection.cursor() as cursor:
#             sql = 'insert into shengda_university(title, url,date) values(%s, %s, %s)'
#             # 执行sql语句
#             cursor.execute(sql, (title, url1,date))
#             # 事务提交
#             connection.commit()
# finally:
#         # 关闭数据库连接
#     connection.close()


