import ast

with open("non-merged.txt", "r") as f:
    content = f.read().strip()

intervals = ast.literal_eval(content)

# 1️⃣  Sort once by start time
intervals.sort(key=lambda x: x[0])

# 2️⃣  Merge in a single forward pass
merged = [intervals[0]]
for start, end in intervals[1:]:
    #print(start, end, merged)
    last_start, last_end = merged[-1]

    if start <= last_end:                     # overlap
        merged[-1][1] = max(last_end, end)
        
    else:
        
        # merged[-1][0] = min(end, last_end)
        # merged[-1][1] = max(start, last_start)
        print(start, end)
        merged.append([start, end])
        
            

print("Merged intervals:", merged)

gaps = []
for i in range(1, len(merged)):
    gaps.append([merged[i-1][1], merged[i][0]])
    
print("Gaps:", gaps)