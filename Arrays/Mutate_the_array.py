a=[4,0,1,-2,3]
n=len(a)
b=[]
for i in range(n):
    print(a[i])
    if (i == 0):
        m = 0 + a[0 + a[1]]
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