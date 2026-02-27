import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    p = list(map(int, input().split()))
    
    # middle deque
    mid = p[x:y]
    l, r = 0, len(mid) - 1
    
    # pool = freely rearrangeable numbers
    pool = p[:x] + p[y:]
    pool.sort()
    i = 0
    
    ans = []
    
    while i < len(pool) or l <= r:
        candidates = []
        
        if i < len(pool):
            candidates.append(("pool", pool[i]))
        if l <= r:
            candidates.append(("front", mid[l]))
            candidates.append(("back", mid[r]))

        src, val = min(candidates, key=lambda x: x[1])
        ans.append(val)
        
        if src == "pool":
            i += 1
        elif src == "front":
            l += 1
        else:
            r -= 1
    
    print(*ans)