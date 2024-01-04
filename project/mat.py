seats=int(input('enter no of seats you want:-' ))
option=int(input('enter option here'))
match option:
    case 1:
        print('diamond seats')
        amount= seats*200
    case 2:
        print('sliver seats')
        amount= seats*150
    case 3:
        print('sliver seats')
        amount= seats*100
    case _:
        print('invalid option')
        amount =None
print(amount)          


