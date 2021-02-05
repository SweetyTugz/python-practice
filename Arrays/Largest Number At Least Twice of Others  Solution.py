a=[0,0,0,1]
x=max(a)
print(x)
m=a.index(x)
# print(m)
count=0

while x in a:
    a.remove(x)

for i in a:
    if i*2<=x:
        count=count+1
print(count)
if(len(a)==count):
    print(m)