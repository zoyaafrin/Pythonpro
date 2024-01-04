try:
    a=2+'2'
    print(a)
except TypeError:
    print('error handled')
finally :
    print('exception handled')
    