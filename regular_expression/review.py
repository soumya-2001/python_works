from re import*
text="akc7 @Kbcz"

# pattern="[a-z]"
# pattern="[A-Z]"
# pattern="[0-9]"
# pattern="[a-zA-Z0-9]"
pattern="[^a-z]" #exclude a-z
pattern="[^a-zA-Z0-9]" #special characters only


matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
