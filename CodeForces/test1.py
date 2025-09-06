def solve():
    import sys

    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    ns = list(map(int, data[1:]))

    for n in ns:
        results = []
        k = 1
        while 10**k + 1 <= n:
            divisor = 10**k + 1
            if n % divisor == 0:
                x = n // divisor
                results.append(x)
            k += 1

        if not results:
            print(0)
        else:
            results.sort()
            print(len(results))
            print(" ".join(map(str, results)))
solve()
