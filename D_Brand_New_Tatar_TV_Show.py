from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = Counter(a)
    vals = sorted(cnt)
    m = len(vals)
    win = [False] * m
    bad = 0
    r = m - 1
    for i in range(m - 1, -1, -1):
        while vals[r] - vals[i] > k:
            if (not win[r]) and cnt[vals[r]] % 2:
                bad -= 1
            r -= 1
        win[i] = bad > 0
        if (not win[i]) and cnt[vals[i]] % 2:
            bad += 1
    ans = False
    for i in range(m):
        if win[i] or cnt[vals[i]] % 2 == 0:
            ans = True
            break
    print("YES" if ans else "NO")