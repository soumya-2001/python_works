source_word="chicken"
target_word="hen"
sorted_source_word="".join(sorted(source_word))
sorted_target_word="".join(sorted(target_word))
print("Kangaroo Word" if sorted_source_word==sorted_target_word else "Not Kangaroo Word")


