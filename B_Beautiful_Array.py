from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n, x, s, q = map(int, input().split())
    q0 = q
    a = [0 for i in range(n)]
    for i in range(n):
        a[i] = min(x - 1, q)
        q -= a[i]
    a[-1] += q
    q = q0
    curr = sum(i // x for i in a)
    if (curr <= s <= q // x):
        j = 0
        while curr != s:
            curr -= a[-1] // x
            a[-1] += a[j]
            curr += a[-1] // x
            a[j] = 0
            j += 1
        print(*a)
    else:
        print(-1)