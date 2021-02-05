a=[4,3,2,7,8,2,3,1]

# a=[1,1]
c=[]
for i in range(len(a)+1):
    # if(i==0):
    #     i=i+1
    if(i not in a):
        c.append(i)
while 0 in c:
    c.remove(0)
print(c)



# for i in range(len(a)):
#     i=i+1
#     if i not in a:
#         a.append(i)