
#存在问题！
n = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for i in range(0,6):
    if n>arr[i]:
        r+=(n-arr[i])*rat[i]
        print ((n-arr[i])*rat[i])
        n=arr[i]
print (r)
