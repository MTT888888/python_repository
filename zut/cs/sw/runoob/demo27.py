def String(str,l):
    if(l!=0):
        print(str[l-1],end='  ')
        String(str,l-1)
str=input("请输入字符串：")
l=len(str)
String(str,l)
