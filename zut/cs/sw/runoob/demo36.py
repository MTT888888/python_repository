num=int(input("输出1~num范围内的数字："))
l=[]

for n in range(1,num+1):
    for i in range(2,n):
        if(n%i==0):
            break
    else:
        l.append(n)
print(l)
