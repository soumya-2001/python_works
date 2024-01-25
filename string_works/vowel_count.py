text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
for ch in text:
    #if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    if ch in ["a","e","i","o","u"]:
        v_count+=1
print(f"v_count={v_count}")
print(f"Total length of characters={len(text)}")
print(f"c_count={len(text)-v_count}")