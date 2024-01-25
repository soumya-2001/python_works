def factorial(num=0):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return(fact)
print(factorial(6))