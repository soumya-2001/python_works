text="ABCABBDDE"
word_count={}
duplicate_list=[]
for ch in text:
    if ch in word_count: 
        word_count[ch]+=1
        if ch not in duplicate_list:
            duplicate_list.append(ch)
    else:
        word_count[ch]=1
print(f"second recursive character : {duplicate_list[2]}")


        
        
     