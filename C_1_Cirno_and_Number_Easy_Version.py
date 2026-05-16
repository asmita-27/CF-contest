from collections import defaultdict, Counter, deque
import os
import math
import sys


for _ in range(int(input())):
    a, n = map(int, input().split())
    d = input().split()
    res = 10**18
    s = str(a)
    def f(cur, l):
        if len(cur) == l:
            if len(cur) > 1 and cur[0] == '0':
                return 10**18
            return abs(a - int(cur))
        best = 10**18
        for i in d:
            best = min(best, f(cur + i, l))
        return best
    for l in range(1, len(s) + 2):
        res = min(res, f("", l))

    print(res)