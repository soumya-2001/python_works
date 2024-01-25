from re import *

text="ab Cak7@#"

# pattern="\d"  #predefined character for[0-9]
# pattern="\D"  #predefined character for[^0-9] or excluding numbers
# pattern="\w"  #predefined character for alphanumeric or [a-zA-Z0-9]
pattern="\W"  #predefined character for excluding alphanumeric or [^a-zA-Z0-9]



matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())