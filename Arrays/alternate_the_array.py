a=[1,4,6,8,4,5,9]
b=[]

for i in range(len(a)):
    if(i%2==0):
        b.append(a[i])
    else:
        b.append(a[len(a)-i])
print(b)