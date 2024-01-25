# Validate indian mobile number

from re import*

mobile_number=input("Enter Mobile Number")

rule="([+]91)?[0-9]{10}"


matcher=fullmatch(rule,mobile_number)
print("Valid" if matcher!=None else "Invalid")