dengue_list=["ekm","ekm","tsr","tvm","tvm","ekm","tvm","idk","tvm"]
dengue_count={}
for district in dengue_list:
    if district in dengue_count:
        dengue_count[district]+=1
    else:
        dengue_count[district]=1
print(dengue_count)
# print(f"maximum dengue_count is in : {max(dengue_count)}")
srt_dengue_count=sorted(dengue_count,key=lambda k:dengue_count.get(k),reverse=True)
print(srt_dengue_count)

