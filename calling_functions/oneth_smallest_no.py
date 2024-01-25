def oneth_smallest_num(n1,n2):
    last_digit_n1=n1%10
    last_digit_n2=n2%10
    smallest="n1" if last_digit_n1<last_digit_n2 else "n2"
    return smallest
print(oneth_smallest_num(234,987))
print(oneth_smallest_num(209,400))
