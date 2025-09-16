
with open("stock.txt", "r") as f:
    numbers = list(map(int, f.read().split()))

minimum = min(numbers)
short = numbers.index(minimum)
newarr = numbers[short:]
maximum = max(newarr)
print(f"profit = {maximum - minimum}")