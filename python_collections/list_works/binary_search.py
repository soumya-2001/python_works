list=[10,12,4,8,2,9]
list.sort()
element=int(input("Enter number to be searched"))
is_present=False
low=0
upp=len(list)-1
while(low<=upp):
    mid=(low+upp)//2
    if element==list[mid]:
        is_present=True
        break
    elif element<list[mid]:
        upp=mid-1
    elif element>list[mid]:
        low=mid+1
print(is_present)
