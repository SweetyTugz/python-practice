# n1=[1,2,3,0,0,0]
# n2=[1,4,5]
n1=[1]
n2=[]
m=1
n=0

if(len(num1)>m):
    for i in range(len(num1)-m):
        num1.pop()
else:
    if(len(num2)>n):
        for i in range(len(num2)-n):
            num2.pop()

for i in range(n):
    num1.append(num2[i])
print(num1)

# remove_num1=len(num1)-m
# remove_num2=len(num2)-n
#
# for i in range(remove_num1):
#     num1.pop()
# for s in range(remove_num2):
#     num2.pop()
#
# print(num1)
# print(num2)
