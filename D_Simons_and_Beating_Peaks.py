from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pos = [0]*(n+1)
    for i,x in enumerate(a):
        pos[x] = i
    stk = [(0, n-1)]
    ans = 0
    while stk:
        l, r = stk.pop()
        if l >= r:
            continue
        for val in range(n,0,-1):
            p = pos[val]
            if l <= p <= r:
                mx = p
                break
        lft = mx - l
        rgt = r - mx
        ans += min(lft, rgt)
        if lft > rgt:
            stk.append((l, mx-1))
        else:
            stk.append((mx+1, r))
    
    print(ans)
