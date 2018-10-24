l=[]
n=int(input("请输入要分解的数："))
while n!=1:
    for i in range(2,n+1):
        if(n%i==0):
            n=int(n/i)
            l.append(i)
            break
print(l)
