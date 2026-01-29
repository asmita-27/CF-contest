import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a == sorted(a):
        print(-1)
        continue

    mn, mx = min(a), max(a)
    unique_vals = set(a)
    
    ans = float('inf')
    for v in unique_vals:
        ans = min(ans, max(v - mn, mx - v))
    
    print(ans)
