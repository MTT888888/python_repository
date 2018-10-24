m=['a','b','c']
n=[]
for i in range(3):
    if(m[i]!='a' and m[i]!='c'):
        n.insert(i,'x')
    elif(m[i]!='c'):
        n.insert(i,'z')
    else:
        n.insert(i,'y')
print("比赛名单为：\na--",n[0],"\nb--",n[1],"\nc--",n[2])