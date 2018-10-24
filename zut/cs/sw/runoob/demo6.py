def fun(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    funs=[1,1]
    for i in range(2,n):
        funs.append(funs[-1]+funs[-2])
    return funs
print(fun(3))


