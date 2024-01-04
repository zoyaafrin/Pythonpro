import random
out=[]
while len (out)<6:
    out+=[chr(random.randint(65,90))]
    out+=[chr(random.randint(97,122))]
    out+=[chr(random.randint(8,9))]
    random.shuffle(out)
    captcha =''
    for i in out :
        captcha+=i
    print(captcha)


