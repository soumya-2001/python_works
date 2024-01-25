from json import load
f=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\json_work\\rest_countries\\data.json",encoding="utf-8")
data=load(f)
# print(len(data))

# all country names

# all_country_names=[c.get("name") for c in data]
# print(all_country_names)

# independent_countries=[c.get("name") for c in data if c.get("independent")==True]
# print(independent_countries)

# all_regions={c.get("region") for c in data}
# print(all_regions)

# asian country names

# asian_country_names=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_country_names)

# print capital of ukraine

# capital=[c.get("capital") for c in data if c.get("name")=="Ukraine"]
# print(capital)

# country_name & capital

# country_capital=[(c.get("name"),c.get("capital")) for c in data]
# print(country_capital)

# print all country_name and currencies name

# for c in data:
#     if "currencies" in c:
#         currency_data=c.get("currencies")[0]
#         print(currency_data.get("name"),",",c.get("name"))

# print borders of india

# india_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]
# # print(india_borders)
# indian_borders=[c.get("name")for c in data if c.get("alpha3Code") in india_borders]
# print(indian_borders)

# # print country names which have more than four borders

# for c in data:
#     if "borders" in c and len(c.get("borders"))>4:
#         print(c.get("name"))