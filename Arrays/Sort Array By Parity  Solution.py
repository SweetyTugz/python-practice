a=[3,1,2,4]
c=[]
d=[]
for i in range(len(a)):
    if(a[i]%2==0):
        c.append(a[i])
        c.sort()
    else:
        d.append(a[i])
        d.sort()
c=c+d
print(c)