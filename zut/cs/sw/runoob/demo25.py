num=1
sum=0
n=int(input("输出要计算的阶数："))
for i in range(1,n+1):
    num=num*i
    sum+=num
print(sum)