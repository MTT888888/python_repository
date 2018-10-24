# l=[]
# for i in range(1,11):
#     num=int(input("输出第%d个数字："% i))
#     l.append(num)
# l.sort()
# print(l)
a=[]
print("输出10个数字：")
for i in range(10):
   a.append(int(input()))
print("排序前：",a)
for j in range(9):
    for k in range(j+1,10):
        if(a[j]>a[k]):
            a[j],a[k]=a[k],a[j]
print("排序后：",a)
