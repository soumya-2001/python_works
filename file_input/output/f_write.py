# path="C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\output\\years.txt"
# f=open(path,"w")
# f.write("hello")

# path="C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\output\\colours.txt"
# f=open(path,"w")
# colours=["red","green","blue","orange"]
# for c in colours:
#     f.write(c+"\n")

# que:write aa century years from 1800 to 2024 into century years.txt

# path="C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\output\\century_years.txt"
# f=open(path,"w")
# starting_year=1800
# ending_year=2024
# for year in range(starting_year,ending_year+1):
#     if year%100==0:
#         f.write(str(year)+"\n")

# que:write all years from 1800 to 2024 into years.txt
# path="C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\output\\years.txt"
# f=open(path,"w")
# for year in range(1800,2025):
#     f.write(str(year)+"\n")

# que:read all years from years.txt and print leap years

# readpath="C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\output\\years.txt"
# writepath="C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\output\\leap_years.txt"
# fr=open(readpath,"r")
# fw=open(writepath,"w")
# for line in fr:
#     year=int(line.rstrip("\n"))
#     if year%100==0 and year%400==0 or year%100!=0 and year%4==0:
#         fw.write(str(year)+"\n")
