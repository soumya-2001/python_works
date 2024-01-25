# dict={"jan":100,"feb":200,"march":300}
# print(type(dict))
# print(dict)

# employee={"name":"soumya","age":22,"gender":"female"}

# print(employee["name"])
# print(employee["age"])

product={"code":1001,"name":"orange","price":35}
# print(product["price"])
# for k in product.keys():
#     print(k)
# for v in product.values():
#     print(v)

# for k,v in product.items():
#     print(k,v)
    
# print(product.get("price"))

# product["price"]=50
# print(product)

# product.update({"name":"apple"})
# product.update({"name":"orange"})
# print(product)

product.pop("code")
print(product)