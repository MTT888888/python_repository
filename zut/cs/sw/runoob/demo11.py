f1=1
f2=1
list=[1,1]
mounth=int(input("请输入月份:"))
if(mounth==1or mounth==2):
    print("输入有误！")
if(mounth==3 or mounth==4):
        print(f2)
for i in range(3,mounth+1):
    f1,f2=f2,f1+f2
    list.append(f2)
print(list)


