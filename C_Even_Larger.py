t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    pref = 0 
    best = 0 
    for i in range(n):
        if i % 2 == 0:
            cur = pref - a[i]
        else:
            cur = pref + a[i]

        if i >= 1 and cur < best:
            d = best - cur
            ans += d
            if i % 2 == 0:
                a[i] -= d
                cur += d
            else:
                a[i-1] -= d
                pref += d  
                cur += d
 
        if pref > best:
            best = pref
        pref = cur

    print(ans)
