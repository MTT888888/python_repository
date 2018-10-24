def fun(i):
    sum=0
    if(i<=1):
        sum=1
    else:
        sum=i*fun(i-1)
    return sum
print(fun(5))