from re import*
text="kaBczabc 9@7ce"
# pattern="bc"
# pattern="[aby]"

# pattern="[a-e]" #for getting a sequence from a to e  
# pattern="[A-Z]"

# pattern="[a-z]"
# pattern="[a-zA-Z]" #matches all alphabets
# pattern="[0-9]"
# # pattern="@"

# # pattern="[a-zA-Z0-9]" #for all alphanumeric characters
matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())
