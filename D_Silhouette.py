from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    freq = Counter(b)
    vals = sorted(freq)
    if vals[0] != 0:
        print(-1)
        continue
    if len(vals) == 1:
        print(*([1] * n))
        continue
    value = []
    prev = 0
    ok = True
    for i in range(len(vals) - 1):
        diff = vals[i + 1] - vals[i]
        cnt = freq[vals[i]]
        if diff % cnt:
            ok = False
            break
        cur = diff // cnt
        if cur <= prev:
            ok = False
            break
        value.append(cur)
        prev = cur
    if not ok:
        print(-1)
        continue
    value.append(prev + 1)
    mp = {}
    for x, v in zip(vals, value):
        mp[x] = v
    ans = [mp[x] for x in b]
    print(*ans)