# a=[0,1,0,3,12]
# c=[]
# count=0
# for i in range(len(a)):
#     if(a[i]!=0):
#         c.append(a[i])
#     if(a[i]==0):
#         count=count+1
# print(count)
# x=0
# while x < count:
#     c.append(0)
#     x=x+1
# print(c)

a=[0,1,0,3,12]
# for i in range(len(a)):
#     if(a[i]==0):
#         a[i:]
# print(a)
for i in range(len(a)):
    if a[i] == 0:
        a.remove(a[i])
        a.append(0)
print(a)
