num=[1,14,11]
x=0
for i in num:
    if(i/2 or i*2 in num):
        x=1
    else:
        break
print(x)