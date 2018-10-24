from functools import reduce
sum=0
l=[]
n=int(input("n="))
a=int(input("a="))
for i in range(n):
    sum=sum+a
    a=a*10
    l.append(sum)
    print(sum)
t=reduce(lambda x,y:x+y,l)
print("计算结果为：",t)

