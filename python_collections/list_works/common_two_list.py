#find common elements

list1=[9,4,3,10,15]
list2=[5,4,2,3,20]

list1.sort()
list2.sort()
#for i in range(0,len(list1)):
    #for j in range(0,len(list2)):
        #ith_element=list1[i]
        #jth_element=list2[j]
        #difference=jth_element-ith_element
       # if difference==0:
           # print(ith_element)
           

p1,p2=0,0
while(p1<len(list1) and p2<len(list2)):
    if list1[p1]==list2[p2]:
        print(list1[p1])
        p1+=1
        p2+=1
    elif list1[p1]<list2[p2]:
        p1+=1
    else:
        p2+=1
           
