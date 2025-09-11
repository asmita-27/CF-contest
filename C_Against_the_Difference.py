def slve(a, pos=0):
    n = len(a)
    if pos >= n:
        return 0
    
    best = slve(a, pos + 1)
    val = a[pos]
    if val <= n:
        if val == 1:
            best = max(best, 1 + slve(a, pos + 1))
        else:
            count = 1 
            for end_pos in range(pos + 1, n):
                if a[end_pos] == val:
                    count += 1
                    if count == val:
                        best = max(best, val + slve(a, end_pos + 1))
                        break
    
    return best


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(slve(a))
