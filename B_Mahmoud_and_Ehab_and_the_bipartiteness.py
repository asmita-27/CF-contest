from collections import defaultdict, Counter, deque
import os
import math
import sys

n  = int(input())
adj = [[] for _ in range(n + 1)]
lev = [0] * (n + 1)

for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

def dfs(x, hi, pa):
    lev[x] = hi
    for v in adj[x]:
        if v == pa:
            continue
        dfs(v, hi + 1, x)

dfs(1, 0, -1)
odd = 0
for i in range(1, n + 1):
    if lev[i] % 2 == 1:
        odd += 1 
print(odd * (n - odd) - (n - 1))