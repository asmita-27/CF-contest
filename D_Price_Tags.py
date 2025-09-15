from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n,y = map(int,input().split())
    c = list(map(int,input().split()))
    maxC = max(c)

    freq = [0]*(maxC+1)
    for v in c: freq[v] += 1
    pref = [0]*(maxC+1)
    for i in range(1, maxC+1): pref[i] = pref[i-1] + freq[i]

    best = float('-inf')
    for x in range(2, maxC+2):          
        total = 0
        printed = 0
        d = 1
        while True:
            l = (d-1)*x + 1
            if l > maxC: break
            r = min(d*x, maxC)
            cnt = pref[r] - pref[l-1]
            if cnt:
                total += cnt * d
                if cnt > freq[d]:
                    printed += cnt - freq[d]
            d += 1
        best = max(best, total - printed * y)
    print(best)