
def fname(a):
    if a%2==0:
        return True
    else:
        return False
out=filter(fname,[2,5,6,8,10,5])
print(list(out))    