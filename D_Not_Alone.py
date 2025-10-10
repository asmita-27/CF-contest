import sys
input = sys.stdin.readline

INF = 10**30

def triple_cost(x, y, z): 
    m = sorted((x, y, z))[1]
    return abs(x - m) + abs(y - m) + abs(z - m)

def linear_dp_segment(vals): 
    L = len(vals)
    if L == 0:
        return 0
    if L == 1:
        return INF   
    dp = [INF] * (L + 1)
    dp[0] = 0 
    for i in range(2, L + 1): 
        cost_pair = abs(vals[i-2] - vals[i-1])
        if dp[i-2] + cost_pair < dp[i]:
            dp[i] = dp[i-2] + cost_pair 
        if i >= 3:
            cost_tr = triple_cost(vals[i-3], vals[i-2], vals[i-1])
            if dp[i-3] + cost_tr < dp[i]:
                dp[i] = dp[i-3] + cost_tr
    return dp[L]

def solve_one(a):
    n = len(a) 
    all_same = True
    for x in a:
        if x != a[0]:
            all_same = False
            break
    if all_same:
        return 0 
    bad = [False] * n
    for i in range(n):
        prev = a[(i - 1) % n]
        nxt = a[(i + 1) % n]
        if a[i] != prev and a[i] != nxt:
            bad[i] = True
 
    if not any(bad):
        return 0
 
    if all(bad): 
        ans = INF
        for s in range(min(3, n)): 
            rot = [a[(s + i) % n] for i in range(n)] 
            val = linear_dp_segment(rot)
            if val < ans:
                ans = val 
        if n == 2:
            return abs(a[0] - a[1])
        return ans 
    ans = 0
    visited = [False] * n
    for i in range(n):
        if bad[i] and not visited[i]: 
            j = i
            seg = []
            while bad[j] and not visited[j]:
                visited[j] = True
                seg.append(a[j])
                j = (j + 1) % n
            L = len(seg)
            if L == 1: 
                idx = i
                left = a[(idx - 1) % n]
                right = a[(idx + 1) % n]
                ans += min(abs(a[idx] - left), abs(a[idx] - right))
            else: 
                ans += linear_dp_segment(seg)
    return ans

def main():
    t = int(input())
    out_lines = []
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))
        out_lines.append(str(solve_one(a)))
    print("\n".join(out_lines))

if __name__ == "__main__":
    main()
