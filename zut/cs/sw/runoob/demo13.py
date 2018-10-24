list=[]
for a in range(10):
    for b in range(10):
        for c in range(10):
            n=a*100+b*10+c
        if((n>=100)and (n==pow(c,3)+pow(b,3)+pow(a,3))):
             list.append(n)
print(list)
print(len(list))