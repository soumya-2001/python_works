items=["bat","ball","helmet","stumps"]
#longest_word=max(items,key=lambda w:len(w))
#print(longest_word)
#smallest_word=min(items,key=lambda w:len(w))
#print(smallest_word)

max_items=items[0]
for i in range(1,len(items)):
    current_word=items[i]
    if len(max_items)<len(current_word):
        max_items=current_word
print(f"Longest Word = {max_items}")
    
min_items=items[0]
for i in range(1,len(items)):
    current_word=items[i]
    if len(min_items)>len(current_word):
        min_items=current_word
print(f"Smallest Word = {min_items}")

sum=0
for i in range(0,len(items)):
    current_word=items[i]
    sum=sum+len(current_word)
print(f"Total {sum}")
    
    


