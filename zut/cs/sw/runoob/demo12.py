from math import sqrt
leap = 1
list=[]
for m in range(101,201):
    k = int(sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            continue
    if leap == 1:
        list.append(m)
    leap = 1
print(list)
print ("The total is %d" % len(list))