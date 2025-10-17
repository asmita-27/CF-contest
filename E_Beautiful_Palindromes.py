for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    res = []
    
    for _ in range(k):
        last1 = a[-1] if len(a) >= 1 else 0
        last2 = a[-2] if len(a) >= 2 else 0
        
        for val in range(1, n + 1):
            if val != last1 and val != last2:
                res.append(val)
                a.append(val)
                break
    
    print(' '.join(map(str, res)))

 