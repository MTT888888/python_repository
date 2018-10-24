import requests
import os
kv={"user-agent":"Mozilla/5.0"}
url="http://www.duwenzhang.com/wenzhang/lizhiwenzhang/20180518/388882.html"
root="D://pics//"
path=root+url.split('/')[-1]
try:
   if not os.path.exists(root):#检验给出的路径是否真的存在
       os.mkdir(root)
   if not os.path.exists(path):
       r=requests.get(url,params=kv)
       with open(path,'wb') as f:#  'w'表示文本文件，’wb‘表示二进制文件
           f.write(r.content)
           f.close()
           print("文件保存成功！")
   else:
       print("文件保存不成功！")
except:
    print("产生异常！")

