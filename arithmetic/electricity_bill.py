electricity_used=int(input("Enter the amount of electricity consumed"))
voltage=int(input("Enter the voltage"))
usage=int(input("Enter the total hours of usage"))
electricity_rate=int(input("Enter the current electricity rate"))
watts=electricity_used*voltage
kilowatt_hours=(watts*usage)/1000
cost=kilowatt_hours*electricity_rate
print(f"Total cost of electricity bill is Rs.{cost}")