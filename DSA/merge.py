# import ast

# with open("merge.txt", "r") as f:
#     content = f.read().strip()
    
# literal_list = ast.literal_eval(content)
# literal_list.sort(key=lambda x: x[0])

# i=1
# while i<len(literal_list):
#     current_first = literal_list[i][0]
#     current_second = literal_list[i][1]
#     previous_first = literal_list[i-1][0]
#     previous_second = literal_list[i-1][1]
#     print(previous_first, previous_second, current_first, current_second)
    
#     if previous_second > current_first and previous_first < current_second:
#         print(f"here : {previous_first, current_second}")
#         literal_list[i-1] = [min(previous_first, current_first), max(previous_second, current_second)]
#         literal_list.pop(i)
#     else:
#         i+=1
        
    
# print(literal_list)

import ast

with open("merge.txt", "r") as f:
    content = f.read().strip()

intervals = ast.literal_eval(content)

# 1️⃣  Sort once by start time
intervals.sort(key=lambda x: x[0])

# 2️⃣  Merge in a single forward pass
merged = [intervals[0]]
for start, end in intervals[1:]:
    print(start, end, merged)
    last_start, last_end = merged[-1]

    if start <= last_end:                     # overlap
        merged[-1][1] = max(last_end, end)     # extend the current interval
    else:
        merged.append([start, end])           # add a new disjoint interval

print("Merged intervals:", merged)
