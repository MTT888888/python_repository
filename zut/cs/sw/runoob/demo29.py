# n=int(input("输出大于10的数："))
# x=str(n)
# for i in range(len(x)-1,-1,-1):
#     print(x[i],end=" ")
num=list(input("输出数字："))
num.reverse()
for i in range(len(num)):
    print(num[i],end=" ")