a=[9,9]
x=len(a)-1
# a[x-1]=a[x-1]+1
# if(a[x-1]>9):
#     m=a[x-1]%10
#     del(a[x-1])
#     a.append(1)
#     a.append(m)
# print(a)


while a[x]==9:
    a[x]=0
    x=x-1

if(x<0):
    a=[1]+a
else:
    a[x]=a[x]+1
print(a)

