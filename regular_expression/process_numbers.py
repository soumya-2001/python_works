from re import*

f=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\regular_expression\\numbers.txt","r")

rule="([+]91)?[0-9]{10}"
 
for line in f:
    number=line.rstrip("\n")
    matcher=fullmatch(rule,number)
    if matcher!=None:
        print(number)