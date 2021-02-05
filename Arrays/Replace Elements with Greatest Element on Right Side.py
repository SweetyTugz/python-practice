a=[17,18,5,4,6,1]
# s="asd"
# print(s[::-1])
# a.reverse()
# print(a)







out = []
for i,val in enumerate(a):
    if i == len(a)-1:
        out.append(-1)
        break
    temp = max(a[i+1:])
    out.append(temp)
return out
print(out)

# b=[]
# for i in a:
#     x=a.index(i)
#     print(x)
#     a.pop(x)
#     # n=max(a)
#     # m=a.index(n)
#     # if(a[i]<n):
#     #     a[i]=n
#     #     a.pop(m)
# print(a)
#
# for i in range(len(a)-1,0,-1):
#      print(i)
