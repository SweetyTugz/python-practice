#arr = [0,3,2,1]
#arr=[3,5,5]
# arr=[2,1]
arr=[1,3,2]
#arr=[0,1,2,1,2]
b=0
x=max(arr)

# u=arr.index(x)
# c=[]
# d=[]
#
# y=u+1
# # print(u)
# count=0
# finals=len(arr)
# final=len(arr)-1
# o=list(set(arr))
# # print(o)
# if(final==2):
#     if(len(o)-1==final):
#         y=u
#
#
# # else:
# #     y=u+1
# # print(y)
# # if(final==2):
# #     if(u==1):
# #         b=1
# # print(final)
# # rr=final-u
#
# p=range(y,finals-1)
# # print(p)
# revrange=reversed(p)
#
# for i in revrange:
#
#     if(arr[i]<arr[i-1]):
#         b=1
#     else:
#         b=0
#     d.append(b)
#
# for i in range(u):
#
#     if(arr[i]<arr[i+1]):
#         b=1
#     else:
#         b=0
#     c.append(b)
# print(c)
# print(d)
# if(len(d)==0 or len(c)==0 ):
#     b=0
# else:
#     if(0 not in c and 0 not in d ):
#         b=1
#     else:
#         b=0
#
# print(bool(b))

class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1