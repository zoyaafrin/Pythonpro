import re
st=' ABCDE2345F'
data=re.findall('[A-Z]{5}\d{4}[A-Z]+',st)
print(data)