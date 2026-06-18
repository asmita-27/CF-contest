from collections import defaultdict, Counter, deque
import os
import math
import sys
from bisect import bisect_left

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    vis =[False]*n
    pos = [-1] *n
    flg = True
    for i in range(n):
        st = bisect_left(b, a[i])
        ok = False
        for j in range(st, n):
            if not vis[j]:
                vis[j] = True
                pos[i] = j
                ok = True
                break
        if not ok:
            flg = False
            break
    if not flg:
        print(-1)
        continue
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if pos[i] > pos[j]:
                ans += 1
    print(ans)