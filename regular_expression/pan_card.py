from re import*

pan_number=input("Enter PAN card number:")

# rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}\d{4}[A-Z]{1}"
rule="[A-Z]{3}[PCAFHT][A-Z]\d{4}[A-Z]"

matcher=fullmatch(rule,pan_number)

print("Invalid" if matcher==None else "Valid")