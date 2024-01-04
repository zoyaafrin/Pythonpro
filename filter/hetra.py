def upper(a):
    if 'A'<=a<='Z':
        return True
    else:
        return False
out=filter (upper,'aBc@15$67DEfgh')
print(list(out))        