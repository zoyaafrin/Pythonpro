a=input('enter a  word')
i=0
count=0
while i<len(a):
    if a[i] in"aeiouAEiOU":
            count+=1
    i+=1
print(count)            