def solve():
    import sys
    
    input = sys.stdin.read
    data = input().strip().split('\n')
    t = int(data[0])
    
    for i in range(1, t + 1):
        line = data[i].split()
        n = int(line[0])
        k = int(line[1])
        
        # Generate deals more efficiently - limit by log(n)
        deals = []
        x = 0
        max_x = 40  # 3^40 > 10^9, so this is safe upper bound
        while x <= max_x and 3**x <= n:
            watermelons = 3**x
            if x == 0:
                cost = 3
            else:
                cost = 3**(x+1) + x * 3**(x-1)
            deals.append((watermelons, cost))
            x += 1
        
        # Key optimization: Use 1D DP with rolling array
        # dp[w] = minimum cost to get exactly w watermelons
        INF = float('inf')
        
        # For each number of deals from 1 to k
        prev_dp = {0: 0}  # 0 watermelons with 0 deals costs 0
        
        for deals_used in range(1, k + 1):
            curr_dp = {}
            
            for watermelons, prev_cost in prev_dp.items():
                if prev_cost == INF:
                    continue
                    
                # Try each deal
                for deal_watermelons, deal_cost in deals:
                    new_watermelons = watermelons + deal_watermelons
                    
                    if new_watermelons <= n:
                        new_cost = prev_cost + deal_cost
                        if new_watermelons not in curr_dp:
                            curr_dp[new_watermelons] = INF
                        curr_dp[new_watermelons] = min(curr_dp[new_watermelons], new_cost)
            
            # Merge current results into previous for next iteration
            for w, cost in curr_dp.items():
                if w not in prev_dp:
                    prev_dp[w] = INF
                prev_dp[w] = min(prev_dp[w], cost)
        
        # Find result
        result = prev_dp.get(n, INF)
        
        if result == INF:
            print(-1)
        else:
            print(result)

solve()