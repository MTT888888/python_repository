x=2
y=1
l=[]
n=int(input("数列的项数："))
for i in range(1,n+1):
    print("数列的第%d数列为："% i,x,'/',y)
    l.append(x / y)
    y,x=x,x+y
print("数列和为：",(sum(l)))



