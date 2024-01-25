from re import*

rule="[0-9]{5}"

f=open("C:\\Users\\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\regular_expression\\train_num.txt","r")
for line in f:
    text=line.rstrip("\n")
    # train_num=text.split(" ")
    # for train_number in train_num:
    #     matcher=fullmatch(rule,train_number)
    #     if matcher!=None:
    #         print(train_number)
    matcher=finditer(rule,text)
    for m in matcher:
        print(m.group())