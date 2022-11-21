def summy(m):
    all=0
    for i in m:
        if type(i)==int:
            all+=i
    return all
 
a=[3,2,1]
b = summy(a)-a[0], summy(a)-a[1], summy(a)-a[-1]
c = tuple(b)
print(c)