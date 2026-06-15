from collections import defaultdict, Counter, deque
import os
import math
import sys
from functools import cache
# INF = 10**18

# def help(n, x):
#     d = {}
#     def dfs(cur, cost):
#         if cost >= d.get(cur, INF):
#             return
#         d[cur] = cost
#         if cur == 0:
#             return
#         dfs(cur // x, cost + 1)
#         r = cur % x
#         if r:
#             add = x - r
#             dfs((cur + add) // x, cost + add + 1)
#     dfs(n, 0)
#     return d
for _ in range(int(input())):
    a, b, x = map(int, input().split())
    ra, rb = [], []
    n, s = a, 0
    while True:
        ra.append((n, s))
        if n == 0: break
        n //= x; s += 1
    n, s = b, 0
    while True:
        rb.append((n, s))
        if n == 0: break
        n //= x; s += 1
    ans = abs(a - b)
    for va, sa in ra:
        for vb, sb in rb:
            c = sa + sb + abs(va - vb)
            if c < ans:
                ans = c
    print(ans)
