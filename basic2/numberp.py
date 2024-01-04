num=int(input('enter a number'))
temp=False
for i in range (2,num):
    if num%i==0:
        temp=True
    if not temp:
        print('prime')
    else:
        print('not prime')           
         
