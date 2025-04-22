t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip() 
    L = s.count('<') 
    a = [0]*n
    a[0] = L + 1 
    ans = list(range(1, n+1))
    ans.remove(a[0])
    mn = mx = a[0] 
    for i, ch in enumerate(s, start=1):
        if ch == '<': 
            cand = max(x for x in ans if x < mn)
        else:  
            cand = min(x for x in ans if x > mx)

        a[i] = cand
        ans.remove(cand)
        mn = min(mn, cand)
        mx = max(mx, cand)

    print(*a)
