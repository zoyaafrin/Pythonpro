def count_digit():
    a=input('enter a number')
    count=0
    for i in a:
        if '0'<=i<='9':
            count+=1
    print(count)
count_digit()
