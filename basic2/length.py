a=[1,9,11,23,65,78,43]
if len(a)%2==0:
    out=0
    for i in a:
        out+=1
    else:
        out=1
        for i in a :
            out*=i
print('out')                 