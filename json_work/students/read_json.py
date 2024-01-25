from json import load
f=open("C:\\Users\\Saumya\\OneDrive\Desktop\\python_works\\language_fundamentals\\json_work\\students.json")
data=load(f)
# print(data)

# all_names=[emp.get("name") for emp in data]
# print(all_names)

# departments={emp.get("department") for emp in data}
# print(departments)

max_salary=max(data,key=lambda d:d.get("salary"))
print(max_salary)