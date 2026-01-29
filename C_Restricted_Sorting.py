import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    if a == b:
        print(-1)
        continue 
    out_of_pos = set()
    for i in range(n):
        if a[i] != b[i]:
            out_of_pos.add(a[i])

    mn = min(a)
    mx = max(a)

    ans = mx - mn
    for v in out_of_pos:
        ans = min(ans, max(v - mn, mx - v))
    
    print(ans) 
