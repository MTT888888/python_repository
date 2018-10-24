n = int(input('enter a number:'))
for i in range(1,n+1,2):
    k = (n-i)//2
    print( ' '* k , '*' * i)

for j in range(n-2,0,-2):
    t = (n-j)//2
    print(' '*t, '*'*j)