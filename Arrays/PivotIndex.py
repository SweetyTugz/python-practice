a=[1,7,3,6,5,6]
sum=0
l=0
for i in a:
    sum=sum+i

for i in range(len(a)):

    if l==sum-a[i]:
        print(i)
    else:
        l=l+a[i]
        sum=sum-a[i]
