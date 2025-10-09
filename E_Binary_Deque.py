from collections import defaultdict, Counter, deque
import os
import math
import sys


def query(l, r, p):
    if l == 0:
        return p[r]
    return p[r] - p[l - 1]

for _ in range(int(input())):
    n, s= map(int, input().split())
    a = list(map(int, input().split()))
    p = [0] * n
    p[0] = a[0]
    for i in range(1, n):
        p[i] = p[i - 1] + a[i]
    ans = float('inf')
    for i in range(n):
        l, r = i, n - 1
        pos = -1
        while l <= r:
            mid = (l + r) // 2
            if query(i, mid, p) <= s:
                pos = mid
                l = mid + 1
            else:
                r = mid - 1
        if pos == -1 or query(i, pos, p) != s:
            continue
        ans = min(ans, n - (pos - i + 1))

    print(-1 if ans == float('inf') else ans)