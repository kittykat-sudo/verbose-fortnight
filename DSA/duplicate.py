with open("duplicate.txt", "r") as f:
    numbers = list(map(int, f.read().split()))
print(numbers)
# match = []
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             match.append(numbers[j])
#             break
    
# print(match)

match = set()
seen = set()

for num in numbers:
    if num in seen:
        match.add(num)
    else:
        seen.add(num)
print(match)
match_list = list(match)

print(match_list)
    