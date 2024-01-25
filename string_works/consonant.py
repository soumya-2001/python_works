text="#@pneumonoultramicroscopicsilicovolcanoconiosis"
c_count=0
for ch in text:
    if ch not in ["a","e","i","o","u"]:
        if ch.isalpha(): #used because # and @ willnot be considered as consonants here
            c_count+=1
print(f"c_count={c_count}")
print(f"Total length of characters={len(text)}")