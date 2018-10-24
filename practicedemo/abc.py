
"""
import collections
jh=collections.namedtuple('User','name age id')
hhh=jh('mtt','21','620502')
print(hhh)

dictory={("name",):"mtt","age":21,"id":1328545,112:176}
print(dictory["name",])
print(dictory[112])
print(len(dictory))
print(str(dictory))
print (type(dictory))
print ("age" in dictory)
print (dictory.pop("id"))
print(str(dictory))
print (dictory.popitem())
"""


"""
dicts={
    "北京":{
         "朝阳":["国贸","CBD"] ,
         "西城":["财政部","统计局"],
         "东城":["三里屯","王府井"]
          },
    "河南":{
        "郑州":["郑大","中工"],
        "开封":["河大","开大"],
        "洛阳":["河科大","洛理工"]
          },
    "甘肃":{
        "兰州":["兰大","交大"],
        "天水":["天水师院","一师"]
    }
    }
for i in dicts["甘肃"]["天水"]:
    print (i)
"""
"""
a, b = 0, 1
while b < 1000:
    print(b,end=',')
    a, b = b, a+b
"""
"""
del fab(n):
if n<1:
    print ("输入有误")
    return -1
if n=1 or n=2:
    return 1
else:
    return fab(n-1)+fab(n-2)
"""
"""
        age=int(input("请输入你家狗狗的年龄："))
        if age<0:
           print ("你逗我呢吧！")
        elif age==1:
            print ("相当于14岁的人!")
        elif age==2:
            print ("相当于22岁的人！")
        else:
            human=22+(age-2)*5
            print ("对应人类年龄",human)
  """
"""
num=7
gus=1
print ("数字猜谜游戏！")
while gus!=num:
    gus=int(input("请输出你猜的数字："))
if gus>num:
    print ("猜的数字大了！")
elif gus==num:
    print ("恭喜你猜对了！")
else:
    print ("猜的数字小了！")
"""
"""
num=int(input("输出一个数字:"))
if num%2==0:
    if num%3==0:
        print (str(num)+"能同时被2和3整除！")
    else:
        print (str(num)+"只能被2整除！")
else:
    if num%3==0:
       print (str(num)+"能被3整除，不能被2整除！")
    else:
        print (str(num)+"不能被2和3整除！")
"""
"""
import random
x=random.choice(range(100))
y=random.choice(range(200))
if x>y:
    print "x大于y:",x
elif x==y:
    print"x等于y:",x+y
else:
    print "x小于y:",y
"""
"""
print ("~~~~~~~~~~数字猜谜游戏！欢迎~~~~~~~~~~~~~")
n=1
i=0
while n!=20:
    n=int(input("输入你的数字："))
    i+=1
    if n==20:
       if i<3:
           print ("哇，这么快就猜对了")
       else:
        print ("你可总算猜对了！")
    elif n<20:
        print ("数字猜小了！")
    else:
        print ("数字猜大了！")
"""
"""
n=1000
sum=0
count=1
while count<n:
    sum+=count
    count+=1
print "1到%d以内的和为:%d"%(n,sum)
"""
"""
var=1
while var==1 :
    num=int(input("请输出一个数字："))
    print("数字为:"+str(num))
"""
"""
count=0
while count<5:
    print(count,"小于5")
    count+=1
else:
    print(count,"大于或等于5")
"""
"""
lauanges=["C","C++","Java","Java","C#"]
for x in lauanges:
    print(x)
"""
"""
sites=["Baidu","Alibaba","Tcent"]
for site in sites:
    if site=="Alibaba":
        print("菜鸟教程！")
        break
    print("循环数据为",site)
else:
    print("循环数据为0！")
print("完成循环！")
"""
"""
for i in range(100):
    print(i,end=(" "))
"""
"""
a=["mtt","0528","2016","Software162" ]
for i in range(len(a)):
    print(i,a[i])
"""
"""
for i in "131473205696":
    if i=='6':
        continue
    print("输出值为：",i)
print("还得继续。。。。。")
var=10
while var>0:
    var-=1
    if var==6:
        continue
    print("输出值为:",var)
"""
"""
for i in range(2,10):
    for j  in range(2,i):
        if i%j==0:
            print("%d等于%d乘于%d:"%(i,j,i//j))
            break
    else:
        print(i,"是质数！")
"""
"""
seq=[12,23,45,67,89,37,90,26]
for i,j in enumerate(seq):
    print(i,j)
"""
"""
i=1
while i<=9:
    j=1
    while j<=i:
        num=i*j
        print("%d*%d=%d"%(i,j,num))
        j+=1
    i+=1
"""
"""
list=[1,2,3,4,5]
it=iter(list)
for x in it:
    print(x)
"""
"""
def area(width,height):
    return width*height
def welcome(name):
    print("welcome",name)
welcome("Runoob")
w=4
h=6
print("width=",w,"height=",h,area(w,h))
"""
"""
def printer(str):
    "打印任何传入的字符串"
    print(str)
printer("我要调用用户自定义的函数")
printer("再次调用同一函数")
"""
"""
def Changeint(a):
    a=10
b=5
Changeint(b)
print(b)
"""
"""
def changme(mylist):
    mylist.append([1,2,3,4,5,6])
    print("函数内取值",mylist)
mylist=[10,20,30]
changme(mylist)
print("函数外取值",mylist)
"""
"""
def printinfo(name,age):
    "cdsfhythyt"
    print("名字",name)
    print("年龄",age)
printinfo(age=21,name="mtt")
"""
"""
def printinfo(arg,*vartuple):
    "gjgngbb"
    print("输出：")
    print(arg)
    for n in vartuple:
        print(n)
    return
printinfo(10)
printinfo(20,30,40)
"""
"""
sum=lambda arg1,arg2:arg1+arg2
print("相加后的值",sum(10,30))
"""
"""
def sum(arg1,arg2):
    total=arg1*arg2
    print("函数内",total)
    return total
total=sum(13,56)
print("函数外",total)
"""
"""
num=3
def fun():
    global num
    print(num)
    num=123
    print(num)
fun()
"""
"""
def outer():
    num=10
    def inner():
        nonlocal num
        num=100
        print(num)
    inner()
    print(num)
outer()
"""
"""
a=10
def test():
    global a
    a=a+1
    print(a)
test()
"""
"""
def printinfo(name,age):
    "fryjyun"
    print("名字",name)
    print("年龄",age)
printinfo(age=22,name="mtt")
"""
"""
def fun(country,province,**kwargs):
    print(country,province,kwargs)
fun("china","gansu",city="tianshui",section="maijishan")
"""
"""
n=lambda x,y:x**2+y**
print(n(2,3))
print(n(y=4,x=2))
a=lambda x=0,y=0:x**2+y**3
print(a(4,8))
print(a(6))
print(a(y=5))
"""
"""
b=1
def ss(a):
    c=a+b
    print(c)
print(b)
ss(11)
"""
"""

a=10
def sum(n):
    global a

    n+=a
    a = 12
    print("a=",a,end=",")
    print("n=",n)
sum(3)
"""
"""
import requests
url = "http://www.baidu.com/img/bd_logol.png"
response=requests.get(url)
img=response.content
with open("baidu.png","wb") as f:
    f.write(img)
"""
"""
import time
t=(2018,5,6,11,59,50,6,120,0)
print(time.asctime(t))
print(time.mktime(t))
print(time.ctime(time.time()))
print(time.gmtime(time.time()))
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %W %H:%M:%S' ,time.localtime(time.time())))
print(time.time())
"""
"""
import calendar
print(calendar.calendar(2018))
print(calendar.setfirstweekday(0))
print(calendar.isleap(2018))
print(calendar.leapdays(2008,2018))
print(calendar.month(2018,5))
print(calendar.monthcalendar(2018,5))
print(calendar.monthrange(2018,5))#不太了解！
t=(2018,5,6,20,20,50,7,126,0)
print(calendar.timegm(t))
print(calendar.weekday(2018,5,7))
"""
"""
t=[90,98,74,65,59]
c=[]
for i in range(5):
    s=t[i]>=90and 'A'or t[i]>=60and 'B'or 'C'
    c.append(s)
print(c)
"""
"""
# from datetime import *
# import time
# print(datetime.today())
# print(datetime.now())
# print(datetime.utcnow())
# print(datetime.fromtimestamp(time.time()))
# print(datetime.utcfromtimestamp(time.time()))
# d=date(2018,5,11)
# from datetime import *
# t=time(17,51,50)
# print(datetime.combine(d,t))
# dt=datetime.strptime("2007-03-04 21:08:12", "%Y-%m-%d %H:%M:%S")
# print(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)
# # print(datetime.ctime())
import time
print (time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time())))
"""
""""
def Add(a,b):
    sum=0
    sum=a*b
    print(sum)
    return sum
f=Add(10,12)
print(f)

m=[1,3]
l=[2,4,6,8]
print([l[i]+m[j] for i in range(len(l)) for j in range(len(m))])
bb=[]
minax=[  [1,2,3,4],
         [3,7,9,0],
         [2,4,6,8]   ]
# print([[a[i] for a in minax] for i in range(4)])
for i in range(4):
    bb.append([a[i] for a in minax])
    print(bb)
s={x:x**2 for x in range(10)}
for k,v in s.items():
    print(k,v)
for t,w in enumerate(['wded','erf','dedf','cbcy']):
    print(t,w)
questions={'name','age','sex','address'}
anwsers={'matongtong','22','nan','zhongyuangongxueyuan'}
for r,c in zip(questions,anwsers):
    print('What\'s your {0} ?     It\'s {1}.'.format(r,c))
for n in reversed(range(0,50,5)):
    print(n)
"""
# c='Hello World\n'
# print(str(c),repr(c))
# print(str(1/7),repr(1/7))
# x,y=10*3.5,10*10
# q='The value of x is '+str(x)+', y is '+str(y)
# print(q)
# for i in range(1,11):
#     print(repr(i).rjust(2),repr(i*i).rjust(3),repr(i*i*i).rjust(4))
# print('***********************************')
# for n in range(1,11):
#     print('{0:2d} {1:3d} {2:4d}'.format(n,n*n,n*n*n))
# w='-3.12'.zfill(7)
# print(w)
# dir={'name':'马茼茼','no':201608040206,'address':'Software Engineering 162'}
# for d,b in dir.items():
#     print('{!s}  =====>   {!s}'.format(d,b))
# print('name:{name:3},no:{no:12},address:{address:30}'.format(**dir))
# import math
# print("The value of PI is %7.4f"%math.pi)
# with open("D:\demo.txt",'r+')as f:
    # print(f.readlines(50))
    # print(f.fileno())
    # print(f.isatty())
    # for j in range(134):
    #     line=next(f)
    #     print("第{0}行 ---- 第{1}   ".format(j,line))
    # f.seek(2,2)
#     f.truncate(5)
#     print(f.readline())
#     print(f.tell())
# f.close()
# import os,sys
# ret=os.access('D:\demo.txt',os.F_OK)
# print('F-ok :{}'.format(ret) )
# ret=os.access('D:\demo.txt',os.R_OK)
# print('R-ok :{}'.format(ret) )
# ret=os.access('D:\demo.txt',os.W_OK)
# print('W-ok :{}'.format(ret))
# ret=os.access('D:\demo.txt',os.X_OK)
# print('X-ok :{}'.format(ret))

# print('当前工作路径：{}'.format(os.getcwd()))
# dirs=os.listdir('D:\JAVA')
# for file in dirs:
#     print(file)
# print(os.listdir(os.getcwd()))
# os.rename('aaa.py','abc.py')
# print('重命名成功！')
# print(os.listdir(os.getcwd()))

# print(os.stat('D:\demo.txt')) #检查文件的信息
"""
class  people :#类定义
    #定义基本属性
    name=''
    age=0
    _weight=0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print('{!s} 说：我今年 {!s} 岁,有 {!s} 斤重。'.format(self.name,self.age,self._weight))
#单继承
class student(people):
    grade=0
    def __init__(self,n,a,w,g):
        #调用父类的构造
        people.__init__(self,n,a,w)
        self.grade=g
        #重写父类的方法
    def speak(self):
        print('{!s} 说：我今年 {!s} 岁,有 {!s} 斤重,这次考了 {!s} 分。'.format(self.name,self.age,self._weight,self.grade))
        #为多继承定义的新类
class speaker():
    topic=''
    name=''
    def __init__(self,n,t):
        self.name=n
        self.topic=t
    def speak(self):
        print('我叫 {!s},我的演讲主题是 {!s}'.format(self.name,self.topic))
        #多重继承
class sample(speaker,student):
        a=''
        def __init__(self,n,a,w,g,t):
            student.__init__(self,n,a,w,g)
            speaker.__init__(self,n,t)
test = sample("Tim",25,80,4,"Python")
test.speak() #方法名同，默认调用的是在括号中排前地父类的方法
"""#类的定义与继承
"""
class Parent:
    def myMethod(self):
        print("调用父类方法")
class Child(Parent):
    def myMethod(self):
        print("调用子方法")
c=Child()#子类实例
c.myMethod()#子类调用重写方法
"""#方法重写
# class JustCounter:
#     __secretCounter=0
#     publicCounter=0
#     def Count(self):
#         self.__secretCounter+=1
#         self.publicCounter+=1
#         print(self.__secretCounter)
# counter=JustCounter()
# counter.Count()
# counter.Count()
# print(counter.publicCounter)


# class Vector:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __str__(self):
#         return 'Vector({0},{1})'.format(self.a,self.b)
#     def __add__(self, other):
#         return Vector(self.a+other.a,self.b+other.b)
# v1=Vector(2,10)
# v2=Vector(5,-2)
# print(v1+v2)

#文件通配符
# import glob
# print(glob.glob("D:\*.txt"))
#数学
# import math
# print(math.sin(math.pi/4),'\n',math.log(1024,2))
# #正则表达式
# import re
# print(re.findall(r'\bf[a-z]*','which foot or hand fell fasteast ?'))
# #随机数
# import random
# print(random.choice(['apple','pear','banana']))
# print(random.sample(range(100),10))
# print(random.random()) #随机float数
# print(random.randrange(6)) #随机int数在制定范围中
#发送电子邮件
# import smtplib
# server=smtplib.SMTP('localhost')
# email=server.sendmail('771718945@qq.com','1143298661@qq.com',
#                       """To:771718945@qq.com
#                        From:1143298661@qq.com
#                        Beware the Ides of March."""  )
# print(email)
#日期和时间

#两数和
"""
m=int(input('输入第一个数：'))
n=int(input('输入第二个数：'))
print('数字{0}和{1}的两数之和为:{2}'.format(m,n,m+n))
"""
#平方根
"""
import cmath
num=int(input('输入一个数：'))
num_sqrt=cmath.sqrt(num)

print('{} 的平方根为 {}+{}j'.format(num,num_sqrt.real,num_sqrt.imag))
"""
#二次方程
"""
import cmath
a=int(input('输入a:'))
b=int(input('输入b:'))
c=int(input('输入c:'))
d=(b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print('方程{0}x**2+{1}x+{2}的解为：\nx1={3} \nx2={4}'.format(a,b,c,sol1,sol2))
"""
#计算三角形面积
"""
a=float(input("输入边长a:"))
b=float(input("输入边长b:"))
c=float(input("输入边长c:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('三角形a={0},b={1},c={2},则面积为；{3}'.format(a,b,c,area))
"""
#产生随机数
"""
import random
print(random.randrange(10))
print(random.random())
print(random.choice(['a',123,'rggtgt']))
print(random.sample(range(100),10))
"""
#摄氏温度转华氏温度
"""
cel=float(input("输入摄氏温度："))#摄氏温度转华氏温度的公式为 celsius * 1.8 = fahrenheit - 32
fah=(cel*1.8)+32
print('{0} 摄氏温度转为华氏温度为 {1}'.format(cel,fah) )
"""
#if语句
"""
num=float(input("输入数字："))
if num>0:
    print('正数')
elif num==0:
    print('零')
else:
    print('负数')
"""
#判断字符串是否为数字
"""
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    # try:
    #     import unicodedata
    #     unicodedata.numeric(s)
    #     return True
    # except (TypeError,ValueError):
    #     pass
    return False
print(is_number('hrjgh'))
print(is_number('1'))
print(is_number('1.3'))
print(is_number('-1.4'))
print(is_number('1e5'))
"""
#判断闰年
"""
year=int(input('输入年份：'))
if (year%4==0):
    if (year%100==0):
        if(year%400==0):
            print('{!s} 是闰年！'.format(year))
        else:
            print('{!s} 不是闰年！'.format(year))
    else:
        print('{!s} 是闰年！'.format(year))
else:
    print('{!s} 不是闰年！'.format(year))
"""
#质数判断
"""
n=int(input("输入一个数："))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print('{0} 不是质数'.format(n))
            print(i,'*',n//i,'=',n)
            break
    else:
        print('{0} 是质数'.format(n))
else:
     print('{0} 不是质数'.format(n))
"""
#阶乘实例
"""
num=int(input("输入数字："))
facorial=1
if num<0:
    print('抱歉，负数没有阶乘！')
elif num==0:
    print('0的阶乘是1')
else:
    for i in range(1,num+1):
        facorial*=i

        print('{0} 的阶乘为：{1}'.format(i,facorial))
"""
# 九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}x{1}={2}\t'.format(i,j,i*j),end=' ')
    print()
"""
#斐波那契数列
"""
def ffff(n):
    list=[]
    a,b=0,1
    while n>0:
        a,b=b,b+a
        list.append(b)
        n-=1
    print(list)
ffff(10)
num=int(input("输入要的项数："))
n1,n2=0,1
count=2
if num<0:
    print('请输入正数！')
elif num==1:
    print(n1)
else:
    print(n1,n2,end=' ')
    while count<num:
        ns=n1+n2
        print(ns,end=' ')
        n1=n2;n2=ns
        count+=1
"""
#阿姆斯特朗数
"""
num=int(input("输入一个数："))
sum=0
n=len(str(num))
temp=num
while temp>0:
    digist=temp%10
    sum+=digist**n
    temp//=10
if num==sum:
    print(num,'是阿姆斯特数')

else:
    print(num,'不是阿姆斯特数')
"""
#十进制变二，八，十六进制
"""
num=int(input("输入数字："))
print("十进制数为：",num)
print("转换为二进制：",bin(num))
print("转换为八进制：",oct(num))
print("转换为十六进制：",hex(num))
"""
#ASCII码与字符串转换
"""
c=str(input("输入字符："))
a=int(input("输入数字："))
print(c,"的ASCII码为",ord(c))
print(a,"的字符为",chr(a))
"""
#最大公约数的算法
"""
def hcf(x,y):
    if(x>y):
        smallier=y
    else:
        smallier=x
    for i in range(1,smallier+1):
        if(x%i==0) and (y%i==0):
            hce=i
    return hce
num1=int(input("输入第一个数："))
num2=int(input("输入第二个数："))
print(num1,'和',num2,'的最大公约数为：',hcf(num1,num2))
"""
#简单的计算器实现
"""
def add(x,y):

    return x+y

def subtract(x,y):

    return x-y

def multiply(x,y):

    return x*y

def divide(x,y):

    return x/y

print("选择计算类型:\t","1.加法计算\t","2.减法计算\t","3.乘法计算\t","4.除法计算")

choice=int(input("输入1/2/3/4："))

n1=int(input("x:"))

n2=int(input("y:"))

if(choice==1):

    print("结果:\t",n1,"+",n2,"=",add(n1,n2))

elif(choice==2):

    print("结果:\t",n1,"-",n2,"=",subtract(n1,n2))

elif(choice==3):

    print("结果:\t",n1,"*",n2,"=",multiply(n1,n2))

elif(choice==4):

    print("结果:",n1,"/",n2,"=",divide(n1,n2))
else:
    print("输入有误吧！")
"""
#生成日历
"""
import calendar
yy=int(input("输入年份："))
mm=int(input("输入月份："))
print(calendar.month(yy,mm))
print(calendar.calendar(yy))
"""
#使用递归斐波那契数列
"""
def Feibo(n):
    if(n<=1):
        return n
    else:
        return Feibo(n-1)+Feibo(n-2)
n=int(input("输入项数："))
if(n<0):
    print("输入正数！")
else:
    print("数列为：")
    for i in range(1,n+1):

        print(Feibo(i),end=' ')
"""
#文件IO
"""
with open("D:\\demo.txt",'wt') as f:

    f.write("张凯杰这妞不错哦！")

with open("D:\\demo.txt","rt") as f:

    print(f.read())

f.close()
"""
#字符串判断
"""
#测试一：
print('测试一')
str="w3cschool.cn"
print(str.isalnum())#判断所有字符都是数字或字母
print(str.isalpha())#判断所有字符都是字母
print(str.isdigit())#判断所有字符都是数字
print(str.islower())#判断所有字符都是小写字母
print(str.isupper())#判断所有字符都是大写字母
print(str.istitle())#判断所有单词都是首字母大写，像标题
print(str.isspace())#判断所有字符都是空白字符,\t,\n
print('_________________________________')
#测试二：
print("测试二")
str='w3cschool'
print(str.isalnum())
print(str.isdigit())
print(str.isalpha())
print(str.islower())
print(str.isupper())
print(str.istitle())
print(str.isspace())
"""
#字符串大小写转换
"""
str='www.W3cschool.cn'
print(str.upper())
print(str.lower())
print(str.capitalize())#把"第一个字母"转换为大写，其余小写
print(str.title()) # 把"每个单词的第一个字母"转化为大写，其余小写
"""
#计算每个月的天数
"""
import calendar
monthday=calendar.monthrange(2018,8)
print(monthday)
"""
#获取昨天的日期
"""
import datetime
today=datetime.date.today()
oneday=datetime.timedelta(days=1)
yesterday=today-oneday
print(yesterday)
"""
#list常用操作
"""
#1，list定义
li=['a','d','ghgdfg','e','dfrthh']
print(li)
print(li[0:-3])
#2.list增加元素
li.append('news')
print(li)
li.insert(2,'matongtong')
print(li)
li.extend(['dsdffg','fgtgtrg','ggrhhhyh','matongtong'])
print(li)
#3.list搜索
print(li.index('matongtong'))
print('matongtong' in li)
#4.list删除元素
li.remove('a')
print(li)
li.remove('matongtong')
print(li)
print(li.pop())
#5.list运算符
li=li+['matongtong']
print(li)
li=[1,2,3,4,5]*2
print(li)
#使用join链接list成为字符串
params={'server':'afhhjj','datebase':'fgthjjuj','id':'safdsfd'}
print(['%s=%s'% (k,v) for k,v in params.items()])
#list分割字符串
li=['gfhh=fggtg','mtt=zkj','ffg=eewe']
s=';'.join(li)
print(s)
print(s.split(';'))
print(s.split(';',0))
#list的映射解析
li=[1,4,7,9]
a=[elem*2 for elem in li]
print(a)
#dictionary中的解析
print(params.keys())
print(params.values())
print(params.items())
print([k for k,v in params.items()])
print([v for k,v in params.items()])
print(['%s=%s'%(k,v) for k,v in params.items()])
#list过滤
li=['a','gghhg','foo','b','c','d','d']
print([e for e in li if e !='b'])
print([e for e in li if len(e )>1])
print([e for e in li if li.count(e)==1])
"""
#正则表达式
"""
import re
print(re.match('www','www.w3cschool.cn').span())
print(re.match('com','www.w3school.cn'))
line='Cats are smarter than dogs.'
obj=re.match(r'(.*)are (.*?).*',line,re.M|re.I )
if obj:
    print('obj.group():',obj.group())
    print('obj.group(1):',obj.group(1))
    print('obj.group(2):',obj.group(2))
else:
    print('No match!')
   """
