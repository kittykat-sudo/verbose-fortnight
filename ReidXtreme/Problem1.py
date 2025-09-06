import sys
sys.setrecursionlimit(1000000)
NEG = -10*30
def solve():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    N = int(next(it)); W = int(next(it))
    # 1-based indexing for features
    h = [0]*(N+1)
    u = [0]*(N+1)
    dep = [0]*(N+1)
    for i in range(1, N+1):
        hi = int(next(it)); ui = int(next(it)); di = int(next(it))
        h[i] = hi; u[i] = ui; dep[i] = di
    # Build forest: parent -> children, collect roots
    children = [[] for _ in range(N+1)]
    # print (children, dep)
    roots = []
    for i in range(1, N+1):
        d = dep[i]
        if d == 0:
            roots.append(i)
        else:
            # assume valid input; if out of range, ignore
            if 1 <= d <= N:
                children[d].append(i)
                #print(children)
    # DFS returns dp array A of size W+1:
    # A[0] = 0 means "take nothing from this subtree".
    # For w > 0, A[w] = best value when node is taken and total weight in subtree is w.
    def dfs(v: int):
        # base: take v alone
        dp = [NEG]*(W+1)
        if h[v] <= W:
            dp[h[v]] = u[v]
        # merge children
        for c in children[v]:
            child_dp = dfs(c)
            # collect non-empty weights from child to iterate sparsely
            valid_t = [t for t in range(1, W+1) if child_dp[t] > NEG]
            if not valid_t:
                continue
            b = dp
            # in-place 0/1-like merge, only from states where parent already chosen (w>0 states)
            for w in range(W, -1, -1):
                bw = b[w]
                if bw <= NEG:
                    continue
                rem = W - w
                # add any positive amount from child (t=0 means skip child)
                for t in valid_t:
                    if t > rem:
                        break
                    val = bw + child_dp[t]
                    if val > b[w + t]:
                        b[w + t] = val
        # allow skipping entire subtree
        dp[0] = 0
        return dp
    # Global knapsack over roots (independent forests)
    global_dp = [NEG]*(W+1)
    global_dp[0] = 0
    for r in roots:
        root_dp = dfs(r)
        valid_t = [t for t in range(1, W+1) if root_dp[t] > NEG]
        if not valid_t:
            continue
        g = global_dp
        for w in range(W, -1, -1):
            gw = g[w]
            if gw <= NEG:
                continue
            rem = W - w
            for t in valid_t:
                if t > rem:
                    break
                val = gw + root_dp[t]
                if val > g[w + t]:
                    g[w + t] = val
                    
    print(max(global_dp))
if __name__ == "__main__":
    solve()