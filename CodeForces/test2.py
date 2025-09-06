def solve():
    import sys

    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    
    for i in range(1, t + 1):
        n = int(data[i])
        
        deals = []
        x = 0
        while 3**x <= n:
            watermelons = 3**x
            cost = 3**(x+1) + x * (3**(x-1) if x > 0 else 0)
            deals.append((watermelons, cost))
            x += 1
        
        # Greedy approach: use largest deals first
        deals.reverse()  # Start with largest deals
        
        total_cost = 0
        remaining = n
        
        for watermelons, cost in deals:
            # Use as many of this deal as possible
            times = remaining // watermelons
            total_cost += times * cost
            remaining -= times * watermelons
        
        print(total_cost)

solve()