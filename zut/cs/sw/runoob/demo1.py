count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j)and(j!=k)and(i!=k):
                print("三位数数字为：",i,j,k)
                count+=1
print("总共有",count,"个数字")