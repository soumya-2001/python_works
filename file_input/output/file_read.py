f=open("C:\\Users\Saumya\\OneDrive\\Desktop\\python_works\\language_fundamentals\\file_input\\output\\data.text","r")
# for line in f:
#     print(line)
wc={}
for line in f:
    words=line.rstrip("\n").split(" ")
    for w in words:
        if w in wc:
            wc[w]+=1
        else:
            wc[w]=1
print(wc)