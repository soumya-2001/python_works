text="hello hai hello hai hello" 
lst=text.split(" ")
print(lst)
word_count={}
for w in lst:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)