a=[5,1,2,3,4]
b=a.copy()
a.sort()
count=0
for i in range(len(a)):
    if(a[i]!=b[i]):
        count=count+1
print(count)