import random
num=random.randint(10,20)
while True:
    a=int(input('enter a number:-'))
    if a==num:
        print('congrats: you successfully guessed number',num)
        break 
    elif a<num:
        print('enter greater number')
    elif a>num:
        print('enter lesser number')    
