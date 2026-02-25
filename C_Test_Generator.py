from collections import defaultdict, Counter, deque
import os
import math
import sys

def check(s, m, k):
    need = s
    for i in range(60, -1, -1):
        if (m >> i) & 1:
            val = 1 << i
            take = min(k, need >> i)  
            need -= take * val
            if need == 0:
                return True
    return need == 0
for _ in range(int(input())):
    s, m = map(int, input().split())
    lb = m & -m
    if s % lb != 0:
        print(-1)
        continue
    lo, hi = 1, s
    ans = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(s, m, mid):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)