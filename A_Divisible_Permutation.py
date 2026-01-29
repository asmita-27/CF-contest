from collections import defaultdict, Counter, deque
import os
import math
import sys

t = int(input())
for _ in range(t):
    n = int(input())
    p = [0]*(n+1)
    vis = [False]*(n+1)
    
    p [n] = n
    p[n-1] = 1
    vis[n] = vis[n] = True
    
    for i in range(n-2, 0, -1):
        if p[i+1]+i<=n and not vis[p[i+1]+i]:
            p[i] = p[i+1]+i
        else:
            p[i] = p[i+1]-i
        vis[p[i]] = True
    print(' '.join(map(str, p[1:])))