from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    gaps = []
    for i in range(1, m):
        gaps.append(a[i] - a[i-1] - 1)
 
    wrap_gap = a[0] + n - a[-1] - 1
    if wrap_gap > 0:
        gaps.append(wrap_gap)
 
    gaps.sort(reverse=True)

    ans = 0
    cnt = 0
    for gap in gaps:
        remaining = gap - cnt * 2
        if remaining > 0:
            ans += max(1, remaining - 1)
        cnt += 2

    print(n - ans)