from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    cnt = {}
    for _ in range(n):
        row = list(map(int, input().split()))
        for x in row:
            cnt[x] = cnt.get(x, 0) + 1

    limit = n * (n - 1)
    ok = True
    for v in cnt.values():
        if v > limit:
            ok = False
            break

    print("YES" if ok else "NO")