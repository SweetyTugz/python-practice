# print("asd")

# a = [2,3,5,6]
# map = {1:"one", 2:"two", 3:"three"}

#  item -> map.items()
# val- > map.values()
# map.keys()
# if 1 in map.keys():
#     print("there")
# print(list(map.values())[0])

# if "one" in (map.values()):
#     print("thereee")
# for key,val in enumerate(map):
#     print(val)
#a = "asd"
# print(a[::-1])


# map = {1:"one", 2:"two", 3:"three"}
# # retrieve -> map[0]
# # remove -> map.pop(key)
#
# map.pop(list(map.keys())[1])
# print(map)
# map.
# print(map.popitem())

# a = [2,3,4,5]
# out = [i**3 for i in a]
# map = {i : i**3 for i in a}
# a1 = list(lambda i : i + 3,a)
# print(a1)
# print(map)

# num=[12,345,2,6,7896]
# count=0
# for i in num:
#     x=str(i)
#     if(len(x)%2==0):
#         count=count+1
# print(count)


# print(sorted(x))
# j = 1
# for i in range(0,len(x)-1, j):
#     if x[i] == 0:
#         if i+1 == len(x):
#             break
#         x[i+1] = 0
#         j=2
#     else:
#         j=1
# for i, val in enumerate(x):
#     if val == 0:
#         if i+1 == len(x):
#             break
#         x[i+1] = 0
# print(x)
#
# arr=[0,1,7,6,0,2,0,7]
# arr2=[0,1,9,2,6,0,0,4,1,0]
# arr3=[1,0,2,3,0,4,5,0]
# a=[0,1,2,0,3,4,0,5,6,7,8]
# out = sorted(a,key=lambda x: x)
# print(out)
# a.sort()
# b=set(a)
# print(b)
# a=sorted(set(a))
# a.sort()
# print(a)

# even_a = list(filter(lambda k: a.index(k) % 2 == 0, a))
# odd_a = list(filter(lambda k: a.index(k) % 2 != 0, a))
# print(even_a)
# print(odd_a)



# for i in range(len(a)-1):
#     if a[i]<a[i+1]:
#         del a[i]
# a=sorted(set(a),reverse=True)
# print(a)
# #
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

#
# print(9//2)
#
# x='hello'
# y=x[::-1]

# s="a"
# d=[i for i in s]
# q="b"
# m=[i for i in q]
#
# if(sorted(d)==sorted(m)):
#     print('true')
# else:
#     print('false')

# a="hello"
# b="world"
# print(a+" "+b)
a=((1+2)*3)/4
print(pow(a,5))