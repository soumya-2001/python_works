list=[2,4,5,6,7,8,9]
even=[num for num in list if num%2==0]
print(f"even ={even}")
odd=[num for num in list if num%2!=0]
print(f"odd ={odd}")

num_greater_than5=[num for num in list if num>5]
print(f"num_greater_than5={num_greater_than5}")


c4=["manoj","bilal","akash","malavika","jamina","akshay"]
upper_names=[name.upper() for name in c4]
print(upper_names)

name_less_than6=[name for name in c4 if len(name)>=6 ]
print(name_less_than6)

item=["red","green","blue","white","black","yellow","purple","apple","orange","elephant"]
# item_name=[name for name in item if name[0] in ["a","e","i","o","u"]]
# print(item_name)

item_name=[name for name in item if name[0] not in ["a","e","i","o","u"]]
print(item_name)
