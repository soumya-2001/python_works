from re import*

date=input("Enter a Date")

rule="(0[1-9]|[12][0-9]|3[0-1])-(0[1-9]|1[0-2])-(19|20)[0-9]{2}"

matcher=fullmatch(rule,date)
print("Valid" if matcher!=None else "Invalid")