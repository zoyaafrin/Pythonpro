import re
st='AADST233FwrehrAADST233Fwrweg'
data=re.findall('[A-Z]{5}\d{4}[A-Z]',st)
print(data)