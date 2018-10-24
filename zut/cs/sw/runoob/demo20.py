l=[]
n=int(input("下落的高度为："))
t=int (input("弹跳次数为："))
for i in range(1,t+1):
    n=float(n/2)
    l.append(n)
print("最后一次反弹:",min(l),"m")
print("总共经过",sum(l)*2+100,"m")
