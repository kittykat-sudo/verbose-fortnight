# x = input("Enter a number:")
# print(type(x))

# x = int(x)
# print(type(x))

# for i in range(1,10):
#     print(f"{x}*{i} = ", end="")
#     print(i * x)

# def count_divisible(n, target, arr):
#     divi = sum(1 for num in arr if num%target==0)
#     less = sum(1 for num in arr if num%target==1)
#     big = sum(1 for num in arr if num%target==2)
#     return divi, less, big
  
with open("data.txt", "r") as f:
    numbers = list(map(int, f.read().split()))
print(numbers)

n = numbers[0]
target = numbers[1]
array = numbers[2:]
print(n, target, array)
# count_divisible(n, val, array)
#c = smallest(numbers)
# small = 0
# equal = 0
# large = 0
# for i in range(n):
#     if val > array[i]:
#         small += 1
#     elif val==array[i]:
#         equal+=1
#     else:
#         large+=1
# print(small, equal, large)
# print(sum(1 for num in array if num < val))
for i in range(n):
    num = array[i]
    for i in range(1,n):
        if (target == num+i):
            print(True)
        else:
            continue
    
for num in array:
    diff = target - num
    if 1 <= diff < n:
        print(True)
    


