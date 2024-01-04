import re
st='AP04XC2233 AP33CS4455'
data=re.findall('AP[0-3]\d[A-Z]{2}\d{4}',st)
print(data)