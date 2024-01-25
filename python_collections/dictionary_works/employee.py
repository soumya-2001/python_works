employee={"id":1000,"name":"hari","department":"developer"}
employee["department"]="seniordeveloper"
print(employee)

#if salary not present add salary as 45000 else add bonous of 10000

if "salary" not in employee:
    employee["salary"]=45000
else:
    employee["salary"]+=10000
print(employee)