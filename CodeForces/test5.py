def solve():
    import sys
    
    input = sys.stdin.read
    data = input().split()
    idx = 0
    
    t = int(data[idx])
    idx += 1
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        q = int(data[idx + 2])
        idx += 3
        
        # Read and sort cards
        vadim = [int(data[idx + i]) for i in range(n)]
        idx += n
        kostya = [int(data[idx + i]) for i in range(m)]
        idx += m
        
        vadim.sort(reverse=True)
        kostya.sort(reverse=True)
        
        # Create prefix sums
        vadim_prefix = [0] * (n + 1)
        for i in range(n):
            vadim_prefix[i + 1] = vadim_prefix[i] + vadim[i]
        
        kostya_prefix = [0] * (m + 1)
        for i in range(m):
            kostya_prefix[i + 1] = kostya_prefix[i] + kostya[i]
        
        # Process queries
        for _ in range(q):
            x = int(data[idx])
            y = int(data[idx + 1])
            z = int(data[idx + 2])
            idx += 3
            
            max_sum = 0
            
            # Optimization: limit the range more aggressively
            max_vadim = min(x, z, n)
            
            for vadim_count in range(max_vadim + 1):
                kostya_count = z - vadim_count
                
                if 0 <= kostya_count <= min(y, m):
                    current_sum = vadim_prefix[vadim_count] + kostya_prefix[kostya_count]
                    max_sum = max(max_sum, current_sum)
            
            print(max_sum)

solve()