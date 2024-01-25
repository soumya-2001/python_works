students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
]
# 1. total number of students
print(f"total number of students : {len(students)}") 

#2.print all student name
all_student_names=[stud.get("name") for stud in students]
print(all_student_names)

# 3. experince above 1 year,print name
for stud in students:
    if stud.get("exp")>1:
        print(stud.get("name"))
        
exp_gt_one=[stud.get("name") for stud in students if stud.get("exp")>1]
print(exp_gt_one)

# 4. print students studing java and python

for stud in students:
    if "java" in stud.get("skills") and "python" in stud.get("skills"):
        print(stud.get("name"))

# 5. print students qualified mca

mca_qualification=[stud.get("name") for stud in students if stud.get("qualification")=="mca"]
print(mca_qualification)

# 6.print most experienced student

most_experience_stud=max(students,key=lambda d:d.get("exp"))
# print(most_experience_stud)
highest_exp=most_experience_stud.get("exp")
exp_studs=[stud.get("name") for stud in students if stud.get("exp")==highest_exp]
print(exp_studs)

# 7. print students names having skills>2

for stud in students:
    if len(stud.get("skills"))>2:
        print(stud.get("name"))

# 8.print names starts with j
for stud in students:
    if stud.get("name").startswith("j"):
        print(stud.get("name"))

# 9.print the most selected skill

skill_count={}
for stud in students:
    skills=stud.get("skills")
    for sk in skills:
        if sk in skill_count:
            skill_count[sk]+=1
        else:
            skill_count[sk]=1
print(skill_count)
