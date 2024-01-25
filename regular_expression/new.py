# starting with k,l,m,n
# second place must be digit and that is divisible by 3
# followed by any number of alphabets and numbers
# no special characters

from re import*

data=input("Enter data")

rule="[k-nK-N][369][a-zA-Z0-9]*"


matcher=fullmatch(rule,data)

print("Invalid" if matcher==None else "Valid")