with open("chocolate.txt", "r") as f:
    numbers = list(map(int, f.read().split()))

m = numbers[0]
numbers = numbers[1:]

numbers.sort()

print(numbers[m-1]-numbers[0])