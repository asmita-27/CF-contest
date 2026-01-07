from collections import defaultdict, Counter, deque
import os
import math
import sys
def solve_one(n, m, k):
    L = k - 1           
    R = n - k           

    if m == 0:
        return 1

    best = 0
    t_max = min(max(L, R), (m + 1) // 2)
    minLR = min(L, R)

    for t in range(t_max + 1):
        max_u = m - 2 * t + 1
        if max_u < 0:
            continue

        u = min(t, max_u, minLR)
 
        if t <= R and u <= L:
            best = max(best, t + u)
 
        if t <= L and u <= R:
            best = max(best, t + u)

    return min(n, 1 + best)


t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    print(solve_one(n, m, k))
