from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    fre = defaultdict(int)
    cst = defaultdict(int)
    for x in a:
        dist = {}
        step = 0
        cur = x
        while cur not in dist:
            dist[cur] = step
            if cur % 2:
                cur += 1
            else:
                cur //= 2
            step += 1
        for v, c in dist.items():
            fre[v] += 1
            cst[v] += c
    ans = float('inf')
    for v in fre:
        if fre[v] == n:
            ans = min(ans, cst[v])

    print(ans)