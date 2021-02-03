#arr=[-2,0,10,-19,4,6,-8]
#arr=[2,3,3,0,0,0]
#arr=[10,2,5,1]
#arr2=[-20,8,-6,-14,0,-19,14,4]
# a=0
# c=[]
# while 0 in arr2:
#     arr2.remove(0)
# print(arr2)
# for i in arr2:
#     a=int(bool(i/2 in arr2 or i*2 in arr2))
#     c.append(a)
# print(c)
# if(1 in c):
#     a=1
# print(bool(a))
a=0
c = []
count=0
for z in arr:
    if(z==0):
        count=count+1
for i in arr:
    if(i!=0):
        a = int(bool(i / 2 in arr or i * 2 in arr))
        c.append(a)
    else:
        if(count>1):
            c.append(1)
        else:
            c.append(0)
if (1 in c):
    a = 1
print(bool(a))