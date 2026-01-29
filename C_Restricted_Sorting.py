import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    # Check if already sorted
    is_sorted = True
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            is_sorted = False
            break
    
    if is_sorted:
        print(-1)
        continue

    mn = min(a)
    mx = max(a)
    
    ans = mx - mn
    for v in set(a):
        ans = min(ans, max(v - mn, mx - v))
    
    print(ans)
