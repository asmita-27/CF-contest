a = []
    for _ in range(n):
        a.extend(map(int, input().split()))
    
    neg = sum(1 for x in a if x < 0)
    total = sum(abs(x) for x in a)
    
    if neg % 2 == 0:
        print(total)
    else:
        min_abs = min(abs(x) for x in a)
        print(total - 2 * min_abs)