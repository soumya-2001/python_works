def is_amstrong(num):
    original=num
    num_str=str(num)
    digit_count=len(num_str)
    sum=0
    while(num!=0):
        digit=num%10
        expo=digit**digit_count
        sum+=expo
        num=num//10
    return("Amstrong" if sum==original else "Not Amstrong")
print(is_amstrong(1634))