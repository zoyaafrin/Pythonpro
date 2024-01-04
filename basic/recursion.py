a=(4,7,6,2)
def add_int(var,i=0):
    if len(var)-1==i:
        return var[i]
    return var [i] +add_int(var,i+1)
out=add_int(a)
print (out)