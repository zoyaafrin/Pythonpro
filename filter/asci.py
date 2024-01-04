def data_filter(a):
    if 'a'<=a<='z':
        return True
    else:
        return False
def ascii(b):
    return ord(b)
out=map(ascii,filter(data_filter,'a1b2c3Def12@#9Z'))
print(list(out))
