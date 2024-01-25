list=[3,4,5,2]
#sum=int(input("Enter Sum"))
#list.sort()
#count=1
#for i in range(0,len(list)-1):
   # for j in range(i+1,len(list)):
    #    cur_sum=list[i]+list[j]
    #    if sum==cur_sum:
    #        print(list[i],list[j])
   #         break
 #       count+=1
#print("loop count",count)

sum=int(input("Enter Sum"))
list.sort()
low=0
count=1
upp=len(list)-1
while(low<upp):
    cur_sum=list[low]+list[upp]
    if cur_sum==sum:
        print(list[low],list[upp])
        break
    elif cur_sum<sum:
        low+=1
    elif cur_sum>sum:
        upp-=1
    
    count+=1
print("loop count",count) 