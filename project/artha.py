op1=int(input('enter  op:-'))
op2= int(input('enter  op2:-'))
operator=(input ('enter a operator'))
match operator:
    case '+' :
        print('op1+op2')
    case '-' :
        print('op1-op2')
    case '*' :
        print('op1*op2')
    case _:
        print('check operator')    
            