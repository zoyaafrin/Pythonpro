import re
st='The 9 data 5 is 04/01/2024'
data=re.findall('\d{2}',st)
print(data)
