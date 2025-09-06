def solve():
    import sys
    
    input = sys.stdin.read
    data = input().strip().split('\n')
    t = int(data[0])
    
    for i in range(1, t + 1):
        line = data[i].split()
        n = int(line[0])
        k = int(line[1])

        deals = []
        x = 0
        while 3**x <= n:
            watermelons = 3**x
            cost = 3**(x+1) + x * (3**(x-1) if x > 0 else 0)
            deals.append((watermelons, cost))
            x += 1
        
        # DP: dp[watermelons][deals_used] = min_cost
        # Use large number as infinity
        INF = float('inf')
        dp = {}
        
        # Base case: 0 watermelons, 0 deals = 0 cost
        dp[(0, 0)] = 0
        
        # Fill DP table
        for deals_used in range(k + 1):
            for watermelons in range(n + 1):
                if (watermelons, deals_used) not in dp:
                    continue
                    
                current_cost = dp[(watermelons, deals_used)]
                
                # Try each deal type
                for deal_watermelons, deal_cost in deals:
                    new_watermelons = watermelons + deal_watermelons
                    new_deals = deals_used + 1
                    
                    if new_watermelons <= n and new_deals <= k:
                        key = (new_watermelons, new_deals)
                        if key not in dp:
                            dp[key] = INF
                        dp[key] = min(dp[key], current_cost + deal_cost)
        
        # Find minimum cost for exactly n watermelons using ≤ k deals
        result = INF
        for deals_used in range(k + 1):
            key = (n, deals_used)
            if key in dp:
                result = min(result, dp[key])
        
        if result == INF:
            print(-1)
        else:
            print(result)

solve()