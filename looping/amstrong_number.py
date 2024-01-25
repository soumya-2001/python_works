num=input("Enter a number")
digit_count=len(num)
num=int(num)
original=num
sum=0
while(num!=0):
    digit=num%10
    expo=digit**digit_count
    sum+=expo
    num=num//10
print(sum)
print("Amstrong" if original==sum else "Not Amstrong")