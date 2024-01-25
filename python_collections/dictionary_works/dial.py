dials={
       "1":["a","b","c"],
       "2":["d","e","f"],
       "3":["g","h","i"]
}
user_input="12"
main_list=[]
for ch in user_input:
       sub_list=dials.get(ch)
       main_list.append(sub_list)
print(main_list[0])
print(main_list[1])
pairs=[(i,j) for i in main_list[0] for j in main_list[1]]
print(pairs)
       
    