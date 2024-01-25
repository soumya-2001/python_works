all_student_path=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\student.txt","r")
all_failed_path=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\failed.txt","r")

# for st in all_student_path:
#        students=st.rstrip("\n")
#        all_students.add(students)
       
all_students_set={st.rstrip("\n") for st in all_student_path}
# for st in all_failed_path:
#         failed_students=st.rstrip("\n")
#         failed_students.add(failed_students)

failed_students_set={st.rstrip("\n") for st in all_failed_path}
passed_students=all_students_set-failed_students_set
print(passed_students)
        