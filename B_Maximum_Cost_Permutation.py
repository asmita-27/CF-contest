from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    n = int(input().strip())
    p = list(map(int, input().split()))

    def seg(arr):
        L = -1
        R = -1
        for i in range(n):
            if arr[i] != i+1:
                if L == -1:
                    L = i
                R = i
        if L == -1:
            return 0
        return R - L + 1

    zro = [i for i, v in enumerate(p) if v == 0]
    k = len(zro)

    if k == 0:
        print(seg(p))
    elif k == 1:
        pres = set(v for v in p if v != 0)
        ms = (set(range(1, n+1)) - pres).pop()
        p2 = p[:]
        p2[zro[0]] = ms
        print(seg(p2))
    else:
        print(seg(p))