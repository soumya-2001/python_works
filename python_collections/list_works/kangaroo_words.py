source_word="myself"
target_word="self"
source_word_list=[ch for ch in source_word]
target_word_list=[ch for ch in target_word]
for ch in target_word_list:
    if ch in source_word_list:
        source_word_list.remove(ch)
    else:
        print("Not a Kangaroo Word")
        break
else:
    print("Kangaroo Word")