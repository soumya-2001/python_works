n1=int(input("Enter a number"))
n2=int(input("Enter another number"))
sm_no=(n1 if n1<n2 else n2)
fact=1
i=1
while(i<=sm_no):
    if n1%i==0 and n2%i==0:
        fact=i
    i+=1
print(fact)