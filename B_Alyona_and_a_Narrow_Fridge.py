from collections import defaultdict, Counter, deque
import os
import math
import sys

def can(k, a, h):
    b = sorted(a[:k], reverse=True)
    need = sum(b[i] for i in range(0, k, 2))
    return need <= h
n,h = map(int, input().split())
a = list(map(int, input().split()))
lo,hi, ans = 0, n, 0
while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid, a, h):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1
print(ans)