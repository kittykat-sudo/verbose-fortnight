import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    q = next(it)
    out = []
    for _ in range(q):
        k = next(it)
        S = [next(it) for _ in range(k)]
        T = [next(it) for _ in range(k)]
        if S[0] != T[0] or S[-1] != T[-1]:
            out.append("NO")
            continue
        dS = [S[i+1] - S[i] for i in range(k-1)]
        dT = [T[i+1] - T[i] for i in range(k-1)]
        dS.sort()
        dT.sort()
        out.append("YES" if dS == dT else "NO")
    print("\n".join(out))

if __name__ == "__main__":
    solve()