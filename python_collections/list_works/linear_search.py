list=[10,2,11,5,7,20]
element=int(input("Enter element to be searched"))
i=0
is_present=False
while(i<len(list)):
    current_element=list[i]
    if current_element==element:
        is_present=True
        break
    i+=1
print(is_present)