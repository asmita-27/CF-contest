from collections import defaultdict, Counter, deque
import os
import math
import sys

n  = int(input())
adj = [[] for _ in range(n + 1)]

for i in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

col = [-1]*(n+1)
cnt =[0,0]

def dfs(u,c):
    col[u] = c
    cnt[c]+=1
    for v in adj[u]:
        if col[v]==-1:
            dfs(v, 1-c)
dfs(1,0)
ans = cnt[0] * cnt[1] - (n - 1)
print(ans)