from json import load
f=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\json_work\\products\\items.json",encoding="utf-8")
data=load(f)

# print(len(data))

# all_categories={p.get("category") for p in data}
# print(all_categories)

# electronic_products=[p for p in data if p.get("category")=="electronics"]
# print(len(electronic_products))

# jewelery_products=[p for p in data if p.get("category")=="jewelery"]
# print(len(jewelery_products))

costly_product=max(data,key=lambda d:d get("price"))
print(costly_product)