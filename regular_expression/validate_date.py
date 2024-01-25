from re import*

date=input("Enter a date")

rule="(0[1-9]|[12]\d|3[01])"

matcher=fullmatch(rule,date)
print("Valid" if matcher!=None else "Invalid")