selling_price=int(input("Enter the selling price"))
cost_price=int(input("Enter the cost price"))
profit=selling_price-cost_price
print(f"Profit {profit}")
profit_percent=(profit/cost_price)*100
print(f"Profit Percentage {profit_percent} ")
print(f"A product whose cost price {cost_price} sold for rs 2{selling_price} % profit = {profit_percent}")