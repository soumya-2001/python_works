from re import *

variable_name=input("enter variable name")

rule="[a-zA-Z]{1}[a-zA-Z0-9_]*"

matcher=fullmatch(rule,variable_name)
# if (matcher==None):
#     print("Invalid")
# else:
#     print("Valid")

print("invalid" if matcher==None else "valid")