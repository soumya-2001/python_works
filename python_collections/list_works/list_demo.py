#colors=["red","green","blue","white","red",1,True,1.5]
#print(colors[2])
#colors[1]="purple"
#print(colors)


expenses=[12000,13000,23000,24000,25000,32000,23000]
#for i in range(0,len(expenses)):
    #print(expenses[i])

#for exp in expenses:
    #print(exp)
#for i in range(0,len(expenses)):
    #if expenses[i]>15000:
        #print(expenses[i])
        
#for i in range(0,len(expenses)):
    #if expenses[i] in range(15000,25000):
        #print(expenses[i])
        
max_exp=max(expenses)
print(max_exp)
min_exp=min(expenses)
print(min_exp)

total_exp=sum(expenses)
print(f"Total Expenses = {total_exp}")

average_exp=sum(expenses)/len(expenses)
print(f"Average Expenses= {average_exp}")
    