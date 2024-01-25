
def add(n1,n2):
    res=n1+n2
    return res
print(add(2,3))
def sub(n3,n4):
    diff=n3-n4
    return diff
print(sub(5,12))

def smart_sub(n3,n4):
    diff=n3-n4 if n3>n4 else n4-n3  
    return(diff)
print(smart_sub(4,31))
print(smart_sub(9,7))
    
    
    
    
    
    
def mul(n5,n6):
    product=n5*n6
    return product
print(mul(2,10))
def div(n7,n8):
    quo=n7/n8
    return quo
print(div(10,2))
def squ(n9):
    square=n9**2
    return square
print(squ(10))

def check(num):
    res="Even" if num%2==0 else "Odd"
    return(res)
print(check(3))
