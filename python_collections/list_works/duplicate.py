arr=[4,9,5,6,7,9,5,4]
#find duplicate numbers
#arr.sort()
#for i in range(0,len(arr)-1):
   # for j in range(i+1,len(arr)):
      #  ith_element=arr[i]
      #  jth_element=arr[j]
      #  difference=jth_element-ith_element
      #  if difference==0:
      #      print(ith_element)
      
arr.sort()
count=1
i=0
while(i<len(arr)-1):
    j=i+1
    ith_element=arr[i]
    jth_element=arr[j]
    diff=jth_element-ith_element
    if diff==0:
        print(ith_element)
        i=j
    i+=1
            
        
        