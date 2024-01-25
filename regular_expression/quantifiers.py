from re import *

text="aaabcaabbaaaabd1248768954457882345678923456789"

# pattern="a*"  #zero or more occurance of a including zero numbers [a-z]*  [0-9]*
# pattern="a{2}" #getting 2 a's together
# pattern="[0-9]{10}"
# pattern="[0-9]*"
pattern="a{2,4}"   #min 2 max 4
pattern="[0-9]{2,4}"   #min 2 max 4

matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
# print(count)