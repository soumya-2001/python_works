from json import load
f=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\json_work\\currency_exchange\\currency.json",encoding="utf-8")
data=load(f)

source_currency_code=input("Enter Source Currency Code")
target_currency_code=input("Enter Target Currency Code")

amount=int(input("Enter Value"))

conversion_rates=data.get("conversion_rates")

source_currency_code_rates=conversion_rates.get(source_currency_code)
target_currency_code_rates=conversion_rates.get(target_currency_code)

print(source_currency_code_rates)
print(target_currency_code_rates)

res=(amount/source_currency_code_rates)*target_currency_code_rates
print(res)