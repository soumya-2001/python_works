def is_leapyear(year):
    if year%100!=100 and year%4==0 or year%100==0 and year%400==0:
        return True
    else:
        return False
print(is_leapyear(1900))