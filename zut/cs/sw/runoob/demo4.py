year=int(input("year:"))
mouth=int(input("mouth:"))
day=int(input("day:"))
mouths=[0,31,59,90,120,151,181,212,242,273,303,334]
if(0<mouth<12):
    sum=mouths[mouth-1]
else:
    print("Date error!")
sum+=day
l=0
if(year%400==0 or year%4==0 and year%100!=0):
    l=1
if(l==1)and(mouth>2):
    sum+=1
print("The day is the %dth at this year!"% sum)
