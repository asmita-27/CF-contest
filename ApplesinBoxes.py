t = int(input())
out = []
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    mn = min(a)
    mx = max(a)
    g = mx - mn
    cnt_max = a.count(mx)
    S = sum(a) 
    if g > k + 1 or (g == k + 1 and cnt_max > 1):
        out.append("Jerry")
    else: 
        out.append("Tom" if (S & 1) else "Jerry")

print("\n".join(out))