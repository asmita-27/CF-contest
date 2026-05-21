from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    freq = defaultdict(int)
    cost = defaultdict(int)
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
            freq[v] += 1
            cost[v] += c
    ans = float('inf')
    for v in freq:
        if freq[v] == n:
            ans = min(ans, cost[v])

    print(ans)