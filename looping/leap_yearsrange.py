start_year=int(input("Enter Starting Year"))
current_year=2023
i=start_year
while(i<=current_year):
    if i%100==0 and i%400==0 or i%100!=0 and i%4==0:
        print(i)
    i+=1