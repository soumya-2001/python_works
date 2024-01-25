mobile={"id":100,"name":"iphone15","price":100000,"imei":2345,"processor":"apple"}
for k,v in mobile.items():
    print(k,v)
print(mobile.get("name"))
print(mobile.get("price"))
mobile.update({"price":85000})
print(mobile)
mobile.pop("imei")
print(mobile)
mobile.update({"offer":1000})
print(mobile)
mobile["offer"]=1000
mobile["price"]+=100
print(mobile)
print("color" in mobile)
print("name" in mobile)