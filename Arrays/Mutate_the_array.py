a=[9]
n=len(a)
b=[]
for i in range(n):
    print(a[i])
    if (i == 0):
        m = 0 + a[0] + a[1]
        b.append(m)
    else:
        if(i==n-1):
            x = a[i - 1]
            y = a[i]
            z=0
            b.append(x+y+z)
        else:
            b.append( a[i - 1]+a[i]+a[i+1])
    #
    # # x = a[i - 1]
    # # y = a[i]
    # # z = a[+1]
    # # b.append(x+y+z)
print(b)

n=123456
# l=str(n)
# count=0
# m=[int(x) for x in l]
# for i in range(len(m)):
#
#     if(m[i:]%3==0):
#         count=count+1
# print(count)
#
# # pairs=[[3,5],[1,4],[2,4],[7,8],[8,0]]
# # c=[]
# # d=[]
# # for i in range(len(pairs)):
# #     x=pairs[i]
# #     for j in range(len(x)):
# #         c.append(x[j])
# #     for l in range(4):
# #         d.append(c[i])
# #     print(d)
