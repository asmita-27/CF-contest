from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    ans = [0] * n
    for k in range(n):
        w = 0
        v = [0] * n
        u = [0] * n
        mx = 0
        mx2 = 0
        for i in range(1, n):
            ii = (k + i - 1) % n
            mx = max(mx, h[ii])
            v[(k + i) % n] = mx
            ind = (k - i + n) % n
            mx2 = max(mx2, h[ind])
            u[ind] = mx2
        v[k] = 0
        u[k] = 0
        for i in range(n):
            w += min(v[i], u[i])
        ans[k] = w
    print(*ans)