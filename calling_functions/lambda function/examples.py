sum=lambda n1,n2:n1+n2
print(sum(2,3))

largest_number=lambda n1,n2:n1 if n1>n2 else n2
print(largest_number(43,65))

num=lambda n:"+ve" if n>0 else "-ve"
print(num(-2))

num=lambda n:"Even" if n%2==0 else "Odd"
print(num(3))

largest=lambda n1,n2,n3:n1 if n1>n2 and n1>n3 else n2 if n2>n3 else n3
print(largest(2,9,6))