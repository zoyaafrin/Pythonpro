import re
st='The 92 data 54 is 04/01/2024'
data=re.findall('\d[24680]',st)
print(data)