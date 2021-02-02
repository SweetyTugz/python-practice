# num=[1,0,2,3,0,4,5,0]
# x=[]
# c=[]
# x.extend(num)
#
# for i in x:
#     if x[i]==0:
#         c.append(i)
# for j in c:
#     x.insert(j+1,0)
#
# remove=len(x)-len(num)
# x=x[:-remove]
# num=x
# print(num)




# arr=[0,1,7,6,0,2,0,7]
# arr2=[0,1,9,2,6,0,0,4,1,0]
# arr3=[1,0,2,3,0,4,5,0]
# arr4=[0,4,1,0,0,8,0,0,3]
#
# x=len(arr)
# c=[]
# if(0 in arr):
#     for i in range(0,x):
#         if(arr[i]==0):
#             c.append(i)
#     print(c)
#
#
#     for z in c:
#         print(z)
#         if(z<(len(arr)/2)):
#             arr.insert(z+1,0)
#         else:
#             if(arr[z]==0 and arr[z-1]==0):
#                 break
#             else:
#               arr.insert(z+2,0)
#         # if(arr[z]==0 and arr[z-1]==0):
#         #     break
#         # else:
#         #     arr.insert(z+1,0)
#
#         # print(arr)
#     remove=len(arr)-x
#     for i in range(remove):
#         arr.pop()
#
# print(arr)
