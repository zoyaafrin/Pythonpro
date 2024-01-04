a=(input ('enter a word'))
i=0
out =''
while i<len(a):
    if '0'<=a[1]<='9':
        out=out+a[i]
    i+=1
print(out)         