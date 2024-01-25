from re import*

rule="(KL|TN)(-)?[0-9]{2}(-)?[A-Z]{1,2}(-)?[0-9]{4}"

f=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\regular_expression\\vehicle_numbers.txt","r")

for line in f:
    vehicle_number=line.rstrip("\n")
    matcher=fullmatch(rule,vehicle_number)
    if matcher!=None:
        print(vehicle_number)
    