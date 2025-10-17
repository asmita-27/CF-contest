for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    res = []
    
    for _ in range(k):
        lst = a[-1]
        sec = a[-2] if len(a) >= 2 else -1
        
        x = -1
        for val in range(1, min(4, n + 1)):
            if val != lst and val != sec:
                x = val
                break
        if x == -1:
            for val in range(1, n + 1):
                if val != lst and val != sec:
                    x = val
                    break
        
        res.append(x)
        a.append(x)
    
    print(' '.join(map(str, res)))

 