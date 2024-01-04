from functools import reduce 
a=[1,2,3,4]
def add(a,b):
    return a+b
out= reduce(add,a)
print(out)
