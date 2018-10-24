import requests
url="http://m.ip138.com/ip.asp?ip="
try:
    r=requests.get(url+'171.15.198.167')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[-500:-1])
except:
    print("抓取失败！")