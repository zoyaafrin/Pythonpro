def sample(a):
    for i in range(0,len(a)):
        if a[i] in 'aeiouAEIOU':
            yield a[i]
            yield i
out=sample('mother theresa')
res=''
for i in out:
    res+=str(i)           
print(res)