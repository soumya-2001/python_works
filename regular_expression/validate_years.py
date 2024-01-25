# range(1900-2099)

from re import*

year=input("Enter a year")

rule="(19|20)[0-9]{2}"

matcher=fullmatch(rule,year)
print("Valid" if matcher!=None else "Invalid")

