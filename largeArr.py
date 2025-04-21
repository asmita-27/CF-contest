
t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    total = sum(a) 
    pref = [0] * (n + 1)
    for i in range(n):
        pref[i + 1] = pref[i] + a[i]
    
    ans = 0
    for i in range(1, n + 1): 
        req = (x + pref[i - 1] + total - 1) // total
        if req <= k:
            ans += (k - req + 1)
    print(ans)
